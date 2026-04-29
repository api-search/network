---
image: /assets/images/blog/building-an-agent-native-api-catalog.png
layout: post
tags:
- Agent-Readiness
- APIs.io
- Discovery
- Cloudflare Workers
- RFC 9727
- Agent Skills
- AI Agents
- Content Negotiation
- Web Bot Auth
title: Building an Agent-Native API Catalog
---

APIs.io has always been a directory of APIs. Over the last two weeks the directory itself became a consumable interface — built so an AI agent can discover, evaluate, and integrate with any of the **7,000+ APIs and 1,400+ providers** in the network without ever scraping HTML. The work layered eight emerging standards across the `apis.io` hub and its ten subdomain sites — and did it on top of static GitHub Pages with a single Cloudflare Worker, proving the agent-readiness bar is reachable without rebuilding the site.

This is what changed.

## Discovery basics, declared explicitly

Every subdomain in the APIs.io network — `apis.apis.io`, `providers.apis.io`, `capabilities.apis.io`, `schemas.apis.io`, `asyncapi.apis.io`, `json-ld.apis.io`, `rules.apis.io`, `tags.apis.io`, `vocabularies.apis.io`, `examples.apis.io`, plus the `apis.io` hub — now publishes a `robots.txt` that explicitly permits search indexing, AI inference, and AI training. It carries [Cloudflare's Content Signals](https://blog.cloudflare.com/content-signals-policy/) directive alongside the IETF AIPREF working group's draft `Content-Usage` syntax:

```
User-agent: *
Allow: /

Content-Signal: search=yes, ai-input=yes, ai-train=yes
Content-Usage: search=y, ai-input=y, ai-train=y

Sitemap: https://<host>/sitemap.xml
```

Each subdomain also publishes its own `sitemap.xml`. Nothing about APIs.io was ever closed; the difference is that the permission is now machine-readable and stated where crawlers look. AIPREF's `Content-Usage` is still a draft; if the syntax shifts, the change is one file in the build pipeline ([`bootstrap-sites.py`](https://github.com/api-search/network/blob/main/scripts/bootstrap-sites.py)).

## A catalog agents can fetch in one request

The biggest single change is at `/.well-known/api-catalog` — an [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727) linkset that turns the entire catalog into a structured fetch.

`apis.apis.io/.well-known/api-catalog` lists **5,595 APIs** in [RFC 9264](https://www.rfc-editor.org/rfc/rfc9264) JSON Linkset format, **2,532 of them carrying a machine-readable `service-desc`** (OpenAPI, AsyncAPI, or Postman). Each entry has an `anchor` URL plus arrays of `service-desc` (machine-readable descriptions), `service-doc` (human docs), and `describedby` (schemas) links. `providers.apis.io/.well-known/api-catalog` is the parallel index across **1,246 providers**, with each provider's APIs nested under `service-desc`. An agent that wants to know what APIs are catalogued can fetch one URL and parse JSON — no HTML traversal required, no per-page crawl.

The two catalogs are around 4 MB and 2 MB respectively. They're written in two paths — `/.well-known/api-catalog` (the spec URI) and `/.well-known/api-catalog.json` (the same content with a friendlier extension for tools that won't follow extension-less URLs) — so tooling that's strict about either form just works. APIs that have no useful properties (no OpenAPI, no docs, no schemas) are excluded from the linkset; they remain in the Jekyll site for browsing but don't show up in the catalog because they wouldn't carry actionable links. That filter currently drops about 1,500 of the 7,093 cataloged APIs — the kind of profile placeholders that are useful as breadcrumbs but not as agent targets.

## A Cloudflare Worker that speaks agent

A small [Worker](https://blog.cloudflare.com/agent-readiness/) sits in front of `*.apis.io` with four jobs.

**1. `Link` HTTP headers ([RFC 8288](https://www.rfc-editor.org/rfc/rfc8288))** are added to every HTML response:

```
Link: <https://apis.apis.io/.well-known/api-catalog>; rel="api-catalog"; type="application/linkset+json",
      </sitemap.xml>; rel="sitemap"; type="application/xml",
      <https://apis.io/skills/>; rel="agent-skills"; type="application/json",
      <self-url>; rel="alternate"; type="text/markdown"
```

Agents don't need to know the URLs ahead of time — they follow link relations from any entry point, the way humans follow `<a>` tags. The same relations are also expressed in HTML via `<link rel=...>` so HTML parsers can find them without inspecting headers.

**2. The Content-Type on the catalog files** is corrected to `application/linkset+json`. GitHub Pages serves extension-less files as `application/octet-stream`, which most RFC 9727 clients tolerate but some tooling rejects.

**3. Markdown content negotiation.** Hit `https://apis.apis.io/apis/<provider>/<slug>/` with `Accept: text/markdown` and the Worker returns clean structured markdown synthesized from the catalog — title, description, links to OpenAPI / docs / schemas — instead of HTML. Same for provider pages. The pre-render is faster than HTML for the agent, smaller than the HTML page, and removes the parsing tax entirely. Link labels are friendly (`OpenAPI`, `AsyncAPI`, `Postman Collection`, `JSON Schema`) rather than raw MIME types, with the lookup chain `link.title → TYPE_LABELS[type] → section fallback → raw type → href` so the markdown reads naturally regardless of how rich each catalog entry is.

**4. Web Bot Auth observability.** Requests carrying [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) HTTP Message Signatures tagged `tag="web-bot-auth"` (the [Cloudflare/IETF draft](https://blog.cloudflare.com/web-bot-auth/)) come back with three possible states surfaced in response headers:

- `x-bot-auth: none` — no signed-bot claim
- `x-bot-auth: claimed-unverified` — signature present but Cloudflare's edge hasn't verified the key directory
- `x-bot-auth: verified-by-edge` — Cloudflare's `cf-verified-bot: true` is set

Plus `x-bot-auth-keyid: <id>` echoing the keyid the agent declared. Real Ed25519 signature verification (RFC 9421 canonicalization, key fetch from the agent's signature directory) is stubbed for now — the scaffolding gives a clear plug-in point and, more importantly, surfaces signed-bot traffic in production logs so the cost of doing the cryptographic work can be evaluated against actual demand rather than speculation.

## Skills that teach the rest

`apis.io/skills/` is now a small directory of [agentskills.io](https://agentskills.io) `SKILL.md` files served as raw `text/markdown`. An agent can fetch the manifest at `apis.io/skills/index.json` and follow the URLs:

| Resource | URL |
|---|---|
| Manifest | [apis.io/skills/index.json](https://apis.io/skills/index.json) |
| `discover-apis-io` | [apis.io/skills/discover-apis-io/SKILL.md](https://apis.io/skills/discover-apis-io/SKILL.md) |
| `search-apis` | [apis.io/skills/search-apis/SKILL.md](https://apis.io/skills/search-apis/SKILL.md) |
| `fetch-api-spec` | [apis.io/skills/fetch-api-spec/SKILL.md](https://apis.io/skills/fetch-api-spec/SKILL.md) |
| Index page | [apis.io/skills/](https://apis.io/skills/) |

`discover-apis-io` primes an agent with the network's structure — the eleven subdomains, the discovery endpoints, the Content-Signal directive, the `Link` headers. `search-apis` gives a concrete recipe for filtering the catalog by keyword, capability, or tag. `fetch-api-spec` shows how to follow `service-desc` links to pull and parse upstream OpenAPI / AsyncAPI / Postman specs. They're plain markdown — no installer, no build step. Every page across the network advertises the directory with `<link rel="agent-skills">` in the HTML head and a matching `Link` header from the Worker, so agents discover the skills from any entry point.

## From per-provider capabilities to canonical capabilities

Capabilities used to mean "what Snowflake offers" or "what Stripe offers" — useful for browsing one provider, less useful for the question "which providers offer object storage?". So the catalog grew a second axis: **26 canonical capabilities** at `capabilities.apis.io/categories/`, each aggregating implementations across providers. `object-storage` lists S3, Apache Ozone, Backblaze B2, Cloudflare R2, GCS, Azure Blob. `payments` lists Adyen, Affirm, Apple Pay, Mastercard, Square, and a dozen more. `iot` lists eight AWS IoT services plus AGCO Precision Farming and Akri Edge.

The taxonomy was seeded from a clustering pass on the existing capability specs (tag frequency, label-keyword extraction with provider names and noise words stripped, exposed-tool action verbs, Jaccard-similarity tag-set clusters), then refined with hand-tuned matchers in [`canonical-capabilities.yml`](https://github.com/api-search/network/blob/main/_data/canonical-capabilities.yml). A nightly `suggest-categories.py` pass scores every capability against the taxonomy and stores the top suggestions as a review file; the build picks them up unless an `info.categories` field is set on the upstream capability YAML, in which case the manual override wins. Hundreds of capabilities currently auto-classify cleanly. The remaining are niche or cross-cutting and accept per-capability overrides.

## Every page now ships its source

Every detail page across the network — APIs, providers, capabilities, schemas, AsyncAPI specs, JSON-LD documents, Spectral rulesets — embeds its upstream source as a YAML / JSON widget with Prism syntax highlighting, line numbers, in-widget search (with `n` / `N` keyboard navigation), format toggle (YAML ↔ JSON via `js-yaml`), copy, and download.

API pages serve the **OpenAPI spec** rather than the apis.yml entry — the spec is what an agent or developer actually wants. Provider, capability, AsyncAPI, JSON-LD, and Rules pages add a **spec picker** that switches between the page's primary source and any related specs from the same provider — a GitHub provider page lets you swap between `apis.yml` and the OpenAPI for any of its 23 APIs without leaving the page. Specs are fetched on demand, cached per-URL, and Prism re-highlights the new content in place so the page stays light even for AWS-style providers with 100+ APIs.

Schema pages skipped the picker (42,000 schemas × 100+ specs per AWS provider would have grown the schemas repo by hundreds of megabytes). Everything else got it.

## Standards summary

| Standard / pattern | Where it lives |
|---|---|
| `robots.txt` with Cloudflare Content Signals + AIPREF | every subdomain |
| `sitemap.xml` | every subdomain |
| RFC 9727 api-catalog (RFC 9264 JSON linkset) | apis.apis.io, providers.apis.io |
| RFC 8288 `Link` headers | every HTML response (via Worker) |
| Markdown content negotiation (`Accept: text/markdown`) | apis.apis.io/apis/`*/*`/, providers.apis.io/providers/`*`/ |
| Web Bot Auth observability headers (RFC 9421) | every HTML response |
| Agent Skills (agentskills.io) | apis.io/skills/ |
| Source viewer (YAML/JSON/OpenAPI inline + picker) | every detail page |

Eight standards. One static-site stack. One Worker.

## What's still on deck

A few items remain explicitly deferred:

- **Real Web Bot Auth signature verification** — needs Ed25519 in WebCrypto, RFC 9421 canonicalization (~150 lines), and key-directory caching. The observability scaffolding will tell us when there's enough signed traffic to be worth implementing.
- **WebMCP** — Chrome 146+ flag-only behind `navigator.modelContext`. Low ROI today, easy to add later.
- **OAuth Protected Resource metadata (RFC 9728), x402 payments, AP2 mandates, the Universal Commerce Protocol manifest** — only when APIs.io itself offers the underlying capability. Adding metadata for capabilities the site doesn't actually have would mislead agents.
- **Naftiko framework integration** — bonus. The Worker is dependency-free vanilla JavaScript today; if the Naftiko framework's patterns are a fit, the Worker can be retrofitted onto it without restructuring the URL space.

## Why this matters

Search engines reward sites whose content they can read; the next decade's crawlers are agents, and they reward sites whose content they can act on. An agent that visits APIs.io now sees machine-readable signals about what is permitted, a single-fetch catalog of every API, structured markdown on demand, signed-bot observability headers, executable skills it can install on the spot, and inline upstream specs on every page.

The networks that publish their content in machine-first formats — linksets, content negotiation, signed identity, executable skills — get used. The ones that only publish HTML get scraped poorly and ranked accordingly. APIs.io now speaks every protocol an agent is likely to reach for when discovering and evaluating APIs, on top of a static GitHub Pages stack with a single Cloudflare Worker. That is the new bar.
