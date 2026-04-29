---
image: /assets/images/blog/100-new-providers-profiled.png
layout: post
tags:
- Network Update
- Catalog Refresh
- Providers
- APIs
title: 100+ New Providers Profiled
---

The APIs.io catalog grew by 102 providers and 345 APIs this morning — the largest single network refresh since automatic rebuild posts began. The newly profiled entries push the running totals to **1,464 providers** and **7,093 APIs** across the network of subdomain sites.

The growth is broad rather than vertical. The 160 new GitHub repos pulled into `api-evangelist/` this cycle spread across financial services, healthcare, manufacturing, content, and developer tooling, rather than concentrating in any one industry. The category aggregator at [`/categories/`](https://capabilities.apis.io/categories/) refreshed alongside the build, so each of the 26 canonical capability buckets — `object-storage`, `payments`, `monitoring`, `iot`, and the rest — picked up new implementations wherever the new providers fit existing patterns. (Eighteen entries in the upstream `apis.yml` still point at api-evangelist GitHub repos that don't exist; they're tracked but unprofiled, a reminder that the source index occasionally references repositories that haven't shipped yet.)

The rest of the catalog tracked the headline numbers proportionally: **74** new schemas (43,008 total), **61** new Spectral rulesets (718), **43** new JSON-LD documents (2,539), and **7** new AsyncAPI specs (82). The api-catalog at [`/.well-known/api-catalog`](https://apis.apis.io/.well-known/api-catalog) now lists **5,595 APIs** (2,532 with machine-readable OpenAPI, AsyncAPI, or Postman descriptions) and **1,246 providers**.

Every newly profiled provider inherits the agent-readiness work shipped earlier this month — RFC 9727 catalog membership, markdown content negotiation, the source widget, and automatic categorization — without any per-provider intervention. The pipeline picks them up; the network grows.
