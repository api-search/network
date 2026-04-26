// apis.io agent-readiness Worker.
//
// Sits in front of *.apis.io. Four jobs:
//   1. Fix Content-Type for /.well-known/api-catalog -> application/linkset+json.
//   2. Add Link headers (RFC 8288) to HTML responses: api-catalog, sitemap,
//      and an alternate text/markdown advertisement.
//   3. Markdown content negotiation: when Accept prefers text/markdown and the
//      URL is /apis/<provider>/<slug>/ on apis.apis.io or /providers/<slug>/
//      on providers.apis.io, synthesize a markdown response from the cached
//      api-catalog instead of returning HTML.
//   4. Web Bot Auth observability: detect RFC 9421 HTTP Message Signatures
//      tagged "web-bot-auth" (draft-meunier-web-bot-auth-architecture) and
//      surface them in an `x-bot-auth` response header. Verification is
//      stubbed — Cloudflare's edge verdict is consumed when present.
//
// `fetch(request)` from inside a Worker bypasses the Worker route, so it goes
// directly to the GitHub Pages origin. No recursion.

const APIS_CATALOG_URL = "https://apis.apis.io/.well-known/api-catalog";
const PROVIDERS_CATALOG_URL = "https://providers.apis.io/.well-known/api-catalog";
const CATALOG_TTL_SECONDS = 600;

const catalogCache = { apis: null, providers: null };

async function getCatalog(kind) {
  const slot = catalogCache[kind];
  const now = Date.now() / 1000;
  if (slot && now - slot.fetchedAt < CATALOG_TTL_SECONDS) return slot.data;
  const url = kind === "apis" ? APIS_CATALOG_URL : PROVIDERS_CATALOG_URL;
  const r = await fetch(url, { cf: { cacheEverything: true, cacheTtl: 300 } });
  if (!r.ok) return null;
  const data = await r.json();
  catalogCache[kind] = { data, fetchedAt: now };
  return data;
}

function preferMarkdown(accept) {
  if (!accept) return false;
  let mdQ = 0, htmlQ = 0;
  for (const token of accept.split(",")) {
    const parts = token.trim().split(";").map((s) => s.trim());
    const type = parts[0].toLowerCase();
    let q = 1;
    for (const p of parts.slice(1)) {
      if (p.startsWith("q=")) q = parseFloat(p.slice(2)) || 0;
    }
    if (type === "text/markdown") mdQ = Math.max(mdQ, q);
    else if (type === "text/html") htmlQ = Math.max(htmlQ, q);
    else if (type === "text/*") {
      mdQ = Math.max(mdQ, q * 0.9);
      htmlQ = Math.max(htmlQ, q * 0.9);
    }
  }
  return mdQ > 0 && mdQ >= htmlQ;
}

function findEntry(catalog, anchor) {
  if (!catalog || !catalog.linkset) return null;
  return catalog.linkset.find((e) => e.anchor === anchor) || null;
}

const TYPE_LABELS = {
  "application/vnd.oai.openapi": "OpenAPI",
  "application/vnd.aai.asyncapi": "AsyncAPI",
  "application/vnd.postman.collection+json": "Postman Collection",
  "application/schema+json": "JSON Schema",
  "application/ld+json": "JSON-LD",
};

function linkLabel(link, fallback) {
  return link.title || TYPE_LABELS[link.type] || fallback || link.type ||
    link.href;
}

function entryToMarkdown(entry, kind) {
  const lines = [];
  lines.push(`# ${entry.title || entry.anchor}`);
  lines.push("");
  lines.push(`**${kind}:** <${entry.anchor}>`);
  lines.push("");
  if (entry["service-desc"]?.length) {
    lines.push("## Machine-readable descriptions");
    for (const link of entry["service-desc"]) {
      const label = linkLabel(link, "description");
      const type = link.type ? ` — \`${link.type}\`` : "";
      lines.push(`- [${label}](${link.href})${type}`);
    }
    lines.push("");
  }
  if (entry["service-doc"]?.length) {
    lines.push("## Documentation");
    for (const link of entry["service-doc"]) {
      lines.push(`- [${linkLabel(link, "Documentation")}](${link.href})`);
    }
    lines.push("");
  }
  if (entry.describedby?.length) {
    lines.push("## Schemas & related");
    for (const link of entry.describedby) {
      const fallback = link.href.split("/").pop();
      lines.push(`- [${linkLabel(link, fallback)}](${link.href})`);
    }
    lines.push("");
  }
  lines.push("---");
  lines.push("Discovered via [RFC 9727 api-catalog](https://www.rfc-editor.org/rfc/rfc9727).");
  return lines.join("\n");
}

// Web Bot Auth (draft-meunier-web-bot-auth-architecture) observability.
//
// Detects RFC 9421 HTTP Message Signatures with the `tag="web-bot-auth"` marker.
// Cloudflare may verify these at the edge and stamp `cf-verified-bot`; if so we
// trust that. Otherwise the request only "claims" web-bot-auth — we surface
// it but do not treat as authenticated. Full verification (Ed25519 signature
// over the canonical message, key fetch from the agent's directory) is a
// follow-up; this scaffolding gives us logs to drive that work.
function inspectBotAuth(request) {
  const sig = request.headers.get("Signature");
  const sigInput = request.headers.get("Signature-Input");
  const sigAgent = request.headers.get("Signature-Agent");
  const cfVerified = request.headers.get("cf-verified-bot");

  const claimsAuth = !!(sig && sigInput && /tag="web-bot-auth"/.test(sigInput));
  if (!claimsAuth && cfVerified !== "true") return { state: "none" };

  let keyid = null, alg = null;
  if (sigInput) {
    const km = sigInput.match(/keyid="([^"]+)"/);
    if (km) keyid = km[1];
    const am = sigInput.match(/alg="([^"]+)"/);
    if (am) alg = am[1];
  }

  if (cfVerified === "true") {
    return { state: "verified-by-edge", keyid, alg, agent: sigAgent };
  }
  return { state: "claimed-unverified", keyid, alg, agent: sigAgent };
}

function withLinkHeaders(response, url, botAuth) {
  const links = [
    `<https://apis.apis.io/.well-known/api-catalog>; rel="api-catalog"; type="application/linkset+json"`,
    `<${url.origin}/sitemap.xml>; rel="sitemap"; type="application/xml"`,
    `<${url.href}>; rel="alternate"; type="text/markdown"`,
  ];
  const headers = new Headers(response.headers);
  for (const link of links) headers.append("Link", link);
  if (botAuth && botAuth.state !== "none") {
    headers.set("x-bot-auth", botAuth.state);
    if (botAuth.keyid) headers.set("x-bot-auth-keyid", botAuth.keyid);
  }
  // Vary so caches don't poison HTML for markdown clients.
  const vary = headers.get("Vary");
  headers.set("Vary", vary ? `${vary}, Accept` : "Accept");
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}

async function handle(request) {
  const url = new URL(request.url);
  const accept = request.headers.get("Accept") || "";
  const botAuth = inspectBotAuth(request);

  // (1) Fix Content-Type on the api-catalog files.
  if (
    url.pathname === "/.well-known/api-catalog" ||
    url.pathname === "/.well-known/api-catalog.json"
  ) {
    const r = await fetch(request);
    if (!r.ok) return r;
    const body = await r.arrayBuffer();
    const headers = new Headers(r.headers);
    headers.set("Content-Type", "application/linkset+json; charset=utf-8");
    headers.set("Cache-Control", "public, max-age=300");
    return new Response(body, { status: r.status, headers });
  }

  // (3) Markdown content negotiation.
  if (preferMarkdown(accept)) {
    if (url.host === "apis.apis.io") {
      const m = url.pathname.match(/^\/apis\/([^\/]+)\/([^\/]+)\/?$/);
      if (m) {
        const catalog = await getCatalog("apis");
        const entry = findEntry(
          catalog,
          `https://apis.apis.io/apis/${m[1]}/${m[2]}/`,
        );
        if (entry) {
          return new Response(entryToMarkdown(entry, "API"), {
            status: 200,
            headers: {
              "Content-Type": "text/markdown; charset=utf-8",
              "Vary": "Accept",
              "Cache-Control": "public, max-age=300",
              "Link": `<${url.href}>; rel="canonical"`,
            },
          });
        }
      }
    } else if (url.host === "providers.apis.io") {
      const m = url.pathname.match(/^\/providers\/([^\/]+)\/?$/);
      if (m) {
        const catalog = await getCatalog("providers");
        const entry = findEntry(
          catalog,
          `https://providers.apis.io/providers/${m[1]}/`,
        );
        if (entry) {
          return new Response(entryToMarkdown(entry, "Provider"), {
            status: 200,
            headers: {
              "Content-Type": "text/markdown; charset=utf-8",
              "Vary": "Accept",
              "Cache-Control": "public, max-age=300",
              "Link": `<${url.href}>; rel="canonical"`,
            },
          });
        }
      }
    }
  }

  // (2) Pass-through with Link headers on HTML.
  const r = await fetch(request);
  const ct = r.headers.get("Content-Type") || "";
  if (ct.includes("text/html")) {
    return withLinkHeaders(r, url, botAuth);
  }
  if (botAuth.state !== "none") {
    const headers = new Headers(r.headers);
    headers.set("x-bot-auth", botAuth.state);
    if (botAuth.keyid) headers.set("x-bot-auth-keyid", botAuth.keyid);
    return new Response(r.body, {
      status: r.status,
      statusText: r.statusText,
      headers,
    });
  }
  return r;
}

export default {
  async fetch(request) {
    return handle(request);
  },
};
