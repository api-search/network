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
title: Building an Agent-Native API Catalog
---

APIs.io has always been a directory of APIs. Over the last two weeks the directory itself became a consumable interface — built so an AI agent can discover, evaluate, and integrate with any of the 7,000+ APIs and 1,400+ providers in the network without scraping HTML.

This is what changed.

## Discovery basics, declared explicitly

Every subdomain in the APIs.io network — `apis.apis.io`, `providers.apis.io`, `capabilities.apis.io`, `schemas.apis.io`, `asyncapi.apis.io`, `json-ld.apis.io`, `rules.apis.io`, `tags.apis.io`, `vocabularies.apis.io`, `examples.apis.io`, plus the `apis.io` hub — now publishes a `robots.txt` that explicitly permits search indexing, AI inference, and AI training. It carries [Cloudflare's Content Signals](https://blog.cloudflare.com/content-signals-policy/) directive (`search=yes, ai-input=yes, ai-train=yes`) alongside the IETF AIPREF working group's draft `Content-Usage` syntax. Each subdomain also publishes its own `sitemap.xml`. Nothing about APIs.io was ever closed; the difference is that the permission is now machine-readable and stated where crawlers look.

## A catalog agents can fetch in one request

The biggest single change is at `/.well-known/api-catalog` — an [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727) linkset that turns the entire catalog into a structured fetch. `apis.apis.io/.well-known/api-catalog` lists 5,595 APIs in [RFC 9264](https://www.rfc-editor.org/rfc/rfc9264) JSON Linkset format, each with an `anchor` URL and arrays of `service-desc` (machine-readable descriptions — OpenAPI, AsyncAPI, Postman), `service-doc` (human docs), and `describedby` (schemas) links. `providers.apis.io/.well-known/api-catalog` is the parallel index across 1,246 providers. An agent that wants to know what APIs are catalogued can fetch one URL and parse JSON — no HTML traversal required.

## A Cloudflare Worker that speaks agent

A small [Worker](https://blog.cloudflare.com/agent-readiness/) now sits in front of `*.apis.io` with four jobs:

1. **Sets `Link` HTTP headers ([RFC 8288](https://www.rfc-editor.org/rfc/rfc8288))** on every HTML response — `rel="api-catalog"`, `rel="sitemap"`, `rel="agent-skills"`, and `rel="alternate"; type="text/markdown"`. Agents don't need to know the URLs; they follow link relations from any entry point.
2. **Fixes Content-Type** on the api-catalog files to `application/linkset+json`, since GitHub Pages serves extension-less files as `application/octet-stream`.
3. **Performs markdown content negotiation.** Hit `https://apis.apis.io/apis/<provider>/<slug>/` with `Accept: text/markdown` and the Worker returns clean structured markdown synthesized from the catalog — title, description, links to OpenAPI, docs, schemas — instead of HTML. Same for provider pages. No more parsing markup to extract structured fields.
4. **Surfaces Web Bot Auth signals.** Requests carrying [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) HTTP Message Signatures tagged `tag="web-bot-auth"` (the [Cloudflare/IETF draft](https://blog.cloudflare.com/web-bot-auth/)) come back with `x-bot-auth: claimed-unverified` (or `verified-by-edge`) and a `keyid` echoed in the response — so signed agent traffic is observable in logs while real Ed25519 verification is being staged.

## Skills that teach the rest

`apis.io/skills/` is now a small directory of [agentskills.io](https://agentskills.io) `SKILL.md` files: `discover-apis-io`, `search-apis`, `fetch-api-spec`. The first primes an agent with the network's structure; the others give it concrete recipes for finding APIs by keyword and pulling their specs. They are plain markdown — no installer, no build — and the manifest at `apis.io/skills/index.json` lets agents discover them programmatically. Every page across the network advertises the directory via `<link rel="agent-skills">` in the HTML head and a matching `Link:` HTTP header from the Worker.

## From per-provider capabilities to canonical capabilities

Capabilities used to mean "what Snowflake offers" or "what Stripe offers" — useful for browsing one provider, less useful for the question "which providers offer object storage?". So the catalog grew a second axis: 26 canonical capabilities at `capabilities.apis.io/categories/`, each aggregating implementations across providers. `object-storage` lists S3, GCS, Azure Blob, Wasabi, Backblaze. `payments` lists Stripe, Adyen, Square, Mastercard. `iot` lists eight AWS IoT services plus AGCO, Akri.

The taxonomy was seeded from a clustering pass on the existing capability specs, then refined with hand-tuned matchers (tags, label keywords, exposed tool names). Hundreds of capabilities currently auto-classify into a canonical bucket; the remaining are niche or cross-cutting and accept per-capability overrides.

## Every page now ships its source

Every detail page across the network — APIs, providers, capabilities, schemas, AsyncAPI specs, JSON-LD documents, Spectral rulesets — embeds its upstream source as a YAML/JSON widget with Prism syntax highlighting, line numbers, in-widget search, format toggle (YAML ↔ JSON via js-yaml), copy, and download.

API pages serve the OpenAPI spec rather than the apis.yml entry. Provider pages, capability pages, AsyncAPI / JSON-LD / Rules pages add a spec picker that switches between the page's primary source and any related specs from the same provider — a GitHub provider page lets you swap between `apis.yml` and the OpenAPI for any of its 23 APIs without leaving the page. The picker fetches each spec on demand, so the page itself stays light.

## Why this matters

Search engines reward sites whose content they can read; the next decade's crawlers are agents, and they reward sites whose content they can act on. An agent that visits APIs.io now sees machine-readable signals about what is permitted, a single-fetch catalog of every API, structured markdown on demand, signed-bot observability headers, and skills it can install on the spot. The whole stack is static GitHub Pages plus one Worker — proof that the agent-readiness bar is reachable without rebuilding the site.

The work isn't finished. Real Web Bot Auth signature verification, an [x402](https://www.x402.org/) payment endpoint for premium catalog operations, a WebMCP entry point, the Universal Commerce Protocol manifest where it fits, and a richer category taxonomy are all next. But APIs.io now speaks every protocol an agent is likely to reach for when discovering and evaluating APIs — and that is the new bar.
