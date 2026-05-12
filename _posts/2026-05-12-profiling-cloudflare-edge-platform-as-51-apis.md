---
date: '2026-05-12'
image: /assets/images/blog/profiling-cloudflare-edge-platform-as-51-apis.png
layout: post
tags:
- Cloudflare
- Edge Computing
- Workers
- AI Gateway
- Serverless
- Provider Profile
title: Profiling Cloudflare — The Edge Platform as 51 APIs and 5 Capability Domains
---

Cloudflare started as a CDN and DNS provider. Fifteen years later, the developer surface looks nothing like a CDN — it's a full-stack edge platform spanning serverless compute, AI inference, vector search, object storage, SQL databases, KV stores, queues, streams, image and video processing, security, observability, and analytics. Every one of those layers is a separately deployable, separately versioned API, and they're all indexed at [providers.apis.io/providers/cloudflare](https://providers.apis.io/providers/cloudflare/).

The Cloudflare profile in the catalog covers **51 APIs**, organized into **5 capability domains**, with **17 JSON-LD context documents** describing the entities those APIs manipulate and **2 AsyncAPI specs** for the webhook surfaces. It's a useful map of what a modern edge-platform provider's API portfolio looks like in 2026.

### The 5 capability domains

Each capability is a [Naftiko spec](https://github.com/naftiko/framework/wiki/Specification) that composes several APIs into a workflow for a specific persona. Cloudflare's five domains map cleanly to the major decisions a developer makes when building on the platform:

**[Serverless Compute](https://capabilities.apis.io/capabilities/cloudflare-serverless-compute/)** — Workers (the original edge-script runtime), Pages (deployed static sites and full-stack apps), Durable Objects (the stateful primitive that makes coordinated edge logic possible), and Queues (async message passing between Workers). This is the compute layer — what most people think of first when they hear "Cloudflare Workers."

**[Data and Storage](https://capabilities.apis.io/capabilities/cloudflare-data-and-storage/)** — R2 (S3-compatible object storage with no egress fees), D1 (serverless SQLite at the edge), KV (eventually-consistent global key-value), and Hyperdrive (acceleration for traditional databases reached from Workers). The persistence layer that closes the loop on edge compute.

**[AI and ML](https://capabilities.apis.io/capabilities/cloudflare-ai-and-ml/)** — Workers AI (run open-weight models on Cloudflare's GPU fleet at the edge), AI Gateway (observability and rate limiting in front of OpenAI, Anthropic, and any other inference provider), and Vectorize (managed vector search for RAG pipelines). The AI surface Cloudflare added in 2023–2024 and has been hardening since.

**[DNS and Security](https://capabilities.apis.io/capabilities/cloudflare-dns-and-security/)** — the DNS APIs, Turnstile (the CAPTCHA-replacement bot challenge), and Logpush (security and access log streaming). The classic Cloudflare surface, still core to the business.

**[Media and Content](https://capabilities.apis.io/capabilities/cloudflare-media-and-content/)** — Stream (video upload, transcode, and adaptive delivery) and Images (image resize, optimization, and signed URLs). The CDN-adjacent product line aimed at media-heavy applications.

### What's interesting about the breakdown

Two things stand out about how Cloudflare's surface partitions.

First, **the platform shape mirrors the major decisions of a modern application architecture**. When a developer says "I'm building an app," the questions they answer in order are: where does the compute run, where does the data live, how does the AI fit in, how is it secured, and how is media handled. Cloudflare has a coherent answer at every layer, and the capability framing in the catalog reflects that order.

Second, **the AI capability sits at the same level as compute and storage, not buried under "developer tools."** Five years ago Workers AI didn't exist. Today it's a peer of Workers itself in how Cloudflare describes the platform. The capability spec for AI and ML composes three APIs (Workers AI, AI Gateway, Vectorize) into a single workflow — which is exactly the shape of a real-world RAG pipeline: model inference + observability + vector retrieval.

### The 51 APIs up close

A representative subset of the API portfolio, grouped by capability domain:

**Compute:** [Workers API](https://apis.apis.io/apis/cloudflare/cloudflare-workers-api/), [Pages API](https://apis.apis.io/apis/cloudflare/cloudflare-pages-api/), [Durable Objects API](https://apis.apis.io/apis/cloudflare/cloudflare-durable-objects-api/), [Queues API](https://apis.apis.io/apis/cloudflare/cloudflare-queues-api/).

**Data:** [R2 API](https://apis.apis.io/apis/cloudflare/cloudflare-r2-api/), [D1 API](https://apis.apis.io/apis/cloudflare/cloudflare-d1-api/), [KV API](https://apis.apis.io/apis/cloudflare/cloudflare-kv-api/), [Vectorize API](https://apis.apis.io/apis/cloudflare/cloudflare-vectorize-api/).

**AI:** [Workers AI API](https://apis.apis.io/apis/cloudflare/cloudflare-workers-ai-api/), [AI Gateway API](https://apis.apis.io/apis/cloudflare/cloudflare-ai-gateway-api/).

**Security and DNS:** [DNS API](https://apis.apis.io/apis/cloudflare/cloudflare-dns-api/), [WAF API](https://apis.apis.io/apis/cloudflare/cloudflare-waf-api/), [Turnstile API](https://apis.apis.io/apis/cloudflare/cloudflare-turnstile-api/), [Logpush API](https://apis.apis.io/apis/cloudflare/cloudflare-logpush-api/), [Magic Transit API](https://apis.apis.io/apis/cloudflare/cloudflare-magic-transit-api/).

**Account/identity surface:** Accounts, Memberships, Certificates, Users, Zones, IP Addresses, Email Routing, Load Balancing — the management plane.

**Media:** [Stream API](https://apis.apis.io/apis/cloudflare/cloudflare-stream-api/), [Images API](https://apis.apis.io/apis/cloudflare/cloudflare-images-api/), plus the [Spectrum API](https://apis.apis.io/apis/cloudflare/cloudflare-spectrum-api/) for non-HTTP TCP/UDP traffic.

**Analytics and observability:** [GraphQL Analytics API](https://apis.apis.io/apis/cloudflare/cloudflare-graphql-analytics-api/), [Radar API](https://apis.apis.io/apis/cloudflare/cloudflare-radar-api/) (which exposes Cloudflare's view of the internet's traffic patterns to anyone, not just paying customers — one of the more genuinely public-good APIs in the catalog).

### Events, webhooks, and the semantic layer

The Cloudflare profile also carries the integration surfaces that the OpenAPI catalog alone doesn't cover:

**[AsyncAPI specs](https://asyncapi.apis.io/asyncapis/cloudflare/)** — Notifications Webhooks (security alerts, billing events, zone changes) and Stream Webhooks (video upload and processing lifecycle events). Two distinct event-driven surfaces, both indexed in the same shape as the REST APIs.

**[17 JSON-LD context documents](https://json-ld.apis.io/json-ld/cloudflare/)** — semantic descriptions of every major Cloudflare entity: Workers scripts, D1 databases, R2 buckets, DNS zones, AI Gateway providers, Pages deployments, etc. Where the OpenAPI describes the request/response shape, the JSON-LD context describes what those shapes *mean* in a shared vocabulary — useful for agents reasoning about Cloudflare resources alongside resources from other providers.

### What the profile illustrates

Cloudflare is interesting in the catalog because it's the same kind of completeness story as Mastercard or Microsoft Azure — a wide enterprise API surface — but at a very different shape. Mastercard's 101 APIs are dominated by payments lifecycle. Microsoft Azure's 463 APIs are dominated by infrastructure resource management. Cloudflare's 51 sit in a tighter, more deliberately product-shaped portfolio: each API maps to a named Cloudflare product, each capability maps to a developer workflow, and the count is small enough that the entire platform fits on one [provider page](https://providers.apis.io/providers/cloudflare/).

For an integrator deciding between platforms, that shape is itself a useful signal. The catalog page lets you see the whole surface — Workers, AI, R2, D1, the security stack, the media stack — in one view, with each API linked to its OpenAPI spec, its capability composition, and its JSON-LD context. From there it's a five-minute path to a [runnable Naftiko capability spec](https://capabilities.apis.io/capabilities/cloudflare-ai-and-ml/) that exposes Workers AI as a REST API and an MCP server, ready for an agent to consume.

For the full Cloudflare profile: [providers.apis.io/providers/cloudflare](https://providers.apis.io/providers/cloudflare/).
