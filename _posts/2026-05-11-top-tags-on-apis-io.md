---
date: '2026-05-11'
image: /assets/images/blog/top-tags-on-apis-io.png
layout: post
tags:
- Tags
- Discovery
- Search
- Taxonomy
- Network Update
title: The Top Tags You Can Search the APIs.io Network By
---


[tags.apis.io](https://tags.apis.io) is the cross-network tag index. Every provider, API, capability, schema, AsyncAPI spec, JSON-LD context, and Spectral ruleset in the catalog can be tagged, and the tag index aggregates those tags across the whole network — letting you ask "show me everything tagged Payments" or "what's in the Federal Government section" with one click.

We pulled the tag counts across the live network this morning. The catalog currently carries **roughly 12,900 unique tags across 65,000+ items**. Here's what's actually being used to find things.

### The top 20 tags on the network

1. [Analytics](https://tags.apis.io/?q=Analytics) — 7,068
2. [Open Source](https://tags.apis.io/?q=Open+Source) — 4,374
3. [Enterprise](https://tags.apis.io/?q=Enterprise) — 4,213
4. [Linked Data](https://tags.apis.io/?q=Linked+Data) — 3,771
5. [JSON-LD](https://tags.apis.io/?q=JSON-LD) — 3,658
6. [Semantic Web](https://tags.apis.io/?q=Semantic+Web) — 3,643
7. [Marketing](https://tags.apis.io/?q=Marketing) — 3,539
8. [Machine Learning](https://tags.apis.io/?q=Machine+Learning) — 3,432
9. [Platform](https://tags.apis.io/?q=Platform) — 3,427
10. [Cloud](https://tags.apis.io/?q=Cloud) — 3,336
11. [Payments](https://tags.apis.io/?q=Payments) — 3,089
12. [Commerce](https://tags.apis.io/?q=Commerce) — 2,972
13. [CRM](https://tags.apis.io/?q=CRM) — 2,925
14. [Security](https://tags.apis.io/?q=Security) — 2,918
15. [Media](https://tags.apis.io/?q=Media) — 2,886
16. [Financial Services](https://tags.apis.io/?q=Financial+Services) — 2,853
17. [AI](https://tags.apis.io/?q=AI) — 2,818
18. [Sales](https://tags.apis.io/?q=Sales) — 2,718
19. [Customer Service](https://tags.apis.io/?q=Customer+Service) — 2,710
20. [Fintech](https://tags.apis.io/?q=Fintech) — 2,687

Analytics at the top tells you what the catalog is dense in: every provider that publishes schemas for analytics entities (sessions, events, conversions, customers, accounts) adds to the count, and the catalog carries tens of thousands of those schemas. Enterprise at #3 is a similar story — broad provider coverage carrying enterprise-themed schemas through. Linked Data, JSON-LD, and Semantic Web at #4–6 reflect the JSON-LD context collection, which uses that trio consistently across every context document.

### The next 25 tags

Below the top 20 the long tail continues with substantial buckets:

- **Broadcasting** — 2,190
- **Automation** — 2,174
- **IoT** — 2,164
- **Serverless** — 2,117
- **Compliance** — 2,104
- **Monitoring** — 2,099
- **Kubernetes** — 1,913
- **Media Processing** — 1,904
- **Market Data** — 1,838
- **Financial Data** — 1,766
- **Containers** — 1,726
- **Research** — 1,695
- **Collaboration** — 1,684
- **Financial** — 1,649
- **Cloud Computing** — 1,595
- **Messaging** — 1,561
- **Portfolio Analytics** — 1,557
- **Investment Analytics** — 1,535
- **Observability** — 1,503
- **ETL** — 1,437
- **API Governance** — 1,395
- **Big Data** — 1,375
- **Database** — 1,366
- **REST** — 1,346
- **Linting** — 1,344

### How to read the network by tag category

The 12,900 tags cluster into a few useful groups:

**API styles and protocols.** REST (1,346), API Governance (1,395), Linting (1,344), Spectral (1,332), API Management (1,294), Authentication (1,288). The governance trio — API Governance / Linting / Spectral — sits at over 1,300 each because every Spectral ruleset and JSON-LD context carries it.

**Compute and platform.** Cloud (3,336), Platform (3,427), Kubernetes (1,913), Serverless (2,117), Containers (1,726), Cloud Computing (1,595), Amazon Web Services (1,403). Where APIs run.

**Capability domains.** Payments (3,089), Commerce (2,972), CRM (2,925), Marketing (3,539), Sales (2,718), Customer Service (2,710), Fintech (2,687), Financial Services (2,853), Media (2,886), Broadcasting (2,190), IoT (2,164). Vertical slices of the network mapped to real business workflows.

**Data and AI.** Analytics (7,068), Machine Learning (3,432), AI (2,818), Big Data (1,375), Database (1,366), ETL (1,437), Market Data (1,838), Financial Data (1,766), Portfolio Analytics (1,557), Investment Analytics (1,535), Observability (1,503), Monitoring (2,099). The data-flow side of the catalog.

**Open ecosystem.** Open Source (4,374), Linked Data (3,771), JSON-LD (3,658), Semantic Web (3,643), Enterprise (4,213). The semantic-web cluster is large because every JSON-LD context carries the trio; Open Source spans the providers, APIs, capabilities, and schemas that publish under permissive licenses.

### How tags get into the catalog

Every record in the network — provider, API, capability, schema, AsyncAPI, JSON-LD, rule — can carry tags in its YAML front matter. The build pipeline reads those tags from the upstream [api-evangelist](https://github.com/api-evangelist) provider repos and propagates them into the per-record Markdown files in each collection. The [tags.apis.io](https://tags.apis.io) homepage then aggregates them client-side by fetching the search indexes for every site in the network in parallel.

That's why a tag like *Payments* can return results across providers (Stripe, Mastercard, Marqeta), APIs (their individual payment endpoints), capabilities (Mastercard Payment Processing and Checkout, 1Password Secrets Management for payment integrations), schemas (the entities those APIs accept and return), and rules (payment-specific Spectral rulesets) — all from a single filter.

### Browsing vs. filtering

A small note on how to use the tag page in practice: the index is sorted by frequency by default, but the filter box at the top of [tags.apis.io](https://tags.apis.io) is a substring filter against every tag in the network. Typing "kubernetes" narrows it from 12,900 tags to the dozen or so that contain the word — Kubernetes itself, Kubernetes Operators, Kubernetes Services, Kubernetes Networking, etc. — and you can pick the variant you actually want.

For agents working the catalog through the search index, the same tag list is in `search-index.json` on every subdomain — tags are a first-class indexable field, not a presentation flourish.

### What the long tail tells us

12,900 unique tags is a lot. Most of them sit in the long tail — applied to fewer than 50 items each — and that's the more interesting half of the index in some ways. Tags like *Carbon Footprint*, *Click to Pay*, *Real Estate Listings*, *Bill Pay Exchange*, *3D Secure*, *Tokenization* describe specific operational concerns that span small clusters of providers. Searching by them is how you find the providers actually working in a narrow area rather than the broad-category list.

The pattern across the catalog is consistent: the top 20 tags get you the big buckets (Analytics, Payments, Marketing, AI, Kubernetes), and the long tail gets you the specific shape of an integration. Both are queryable from the same index.

For everything: [tags.apis.io](https://tags.apis.io).
