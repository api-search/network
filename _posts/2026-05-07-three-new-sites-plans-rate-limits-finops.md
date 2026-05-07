---
date: 2026-05-07
image: /assets/images/blog/three-new-sites-plans-rate-limits-finops.png
layout: post
tags:
- Network Update
- Plans
- Rate Limits
- FinOps
- FOCUS
- API Commons
title: Three New Sites — Plans, Rate Limits, and FinOps Now Indexed Across the Network
---


The APIs.io network just grew by three sites. Pricing plans, rate limit policies, and FinOps profiles — three of the most operationally important pieces of metadata about an API, and three that have historically been the hardest to find without scraping a developer portal — are now indexed at their own subdomains and surfaced in the top-level navigation.

- [**plans.apis.io**](https://plans.apis.io) — 3,786 pricing-plan documents
- [**rate-limits.apis.io**](https://rate-limits.apis.io) — 3,786 rate-limit policy documents
- [**finops.apis.io**](https://finops.apis.io) — 3,786 FOCUS-aligned FinOps profiles

Each one is a per-provider YAML file living in the upstream [api-evangelist](https://github.com/api-evangelist) repos at `plans/`, `rate-limits/`, and `finops/`, picked up by the build pipeline and rendered into a filterable browse and per-provider detail pages.

### What's actually in there

**Plans** — pricing tiers in the [API Commons Plans](https://apicommons.org) format. Each document carries the named plan tiers (Free, Starter, Pro, Enterprise, etc.), the per-tier line items (per-call pricing, seat pricing, included quotas), the included features, and links to the provider's public pricing page. Stripe has 9 plans documented, HubSpot Marketing Hub has 4, 1Password has 5 (Individual, Families, Teams, Business, Enterprise). Mastercard has one — "API access via partner/B2B contracts only" — which is itself a useful piece of plan metadata.

**Rate Limits** — quota policies in the API Commons Rate Limits format. Each document carries the per-API rate limit ceilings, the metrics they're measured in (requests/minute, tokens, calls/day), the scopes they apply to (account, IP, key), the response codes the provider returns when limits are hit (almost always 429), and the retry policies. The 1Password Events API publishes hard ceilings (600/minute, 30,000/hour); most providers publish softer fair-use language. Either way, it's now indexed in the same shape.

**FinOps** — [FOCUS](https://focus.finops.org)-aligned profiles for every provider. Each document covers the provider's billing model (subscription / consumption / metered), pricing category, billing currency and frequency, the FOCUS columns the provider populates (`ServiceName`, `ServiceCategory`, `PublisherName`, `PricingUnit`, etc.), the metering approach, and the alignment with the FinOps Foundation framework. This is the data a procurement team or FinOps practitioner needs to evaluate cost across vendors — and it's now machine-readable in a single shape across the whole catalog.

### Reconciled vs. scaffold

Of the 3,786 documents in each collection, **503 are reconciled** — they carry real, provider-published values, with `reconciled: true` in the front matter. The remaining 3,372 are scaffolds — the schema is in place with sensible defaults, but the values haven't been verified against the provider's published pricing or rate limits yet. The reconciled set covers most of the providers people actually integrate with: Stripe, HubSpot, 1Password, GitHub, Twilio, Mastercard, and the long tail of payment, identity, and SaaS providers in heavy use.

The scaffold approach is intentional. Having a placeholder document for every provider in the catalog — even one that needs reconciliation — means the schema, the file path, the cross-link, and the build pipeline are all in place. Reconciling a provider is now an edit-this-one-file change rather than a "create the directory, write the schema, plumb it through the build" change. The scaffolded 3,372 will close over time.

### Where they sit in the navigation

The top-level "More" dropdown on every site in the network is now grouped:

- **Specifications** — Schemas, AsyncAPI, JSON-LD, Rules, Vocabularies
- **Operations** — *Plans, Rate Limits, FinOps*

The split reflects what you're actually looking for. Specifications describe what the API *is* (its contracts, schemas, semantic vocabulary). Operations describe what it *costs and constrains* (its pricing, its quotas, its FinOps shape). Both are first-class metadata; they belong as siblings, not as one nested under the other.

### Why three separate sites

The same question came up when AsyncAPI got its own subdomain instead of being tucked under apis.apis.io: why not just embed this data in the provider profile and call it done?

The answer is the same: cross-provider search. "Find me every payments provider that publishes a Free tier with API access" is a question you want to ask across plans, not within one provider's profile. "Find me every provider that publishes hard rate limit ceilings rather than fair-use language" is a question against rate-limits. "Find me every SaaS provider whose FinOps profile aligns to FOCUS v1.3 and uses seat-month as a pricing unit" is a question against finops. Each one is a query across the whole network, in the shape of one specific operational concern, and that's what gets a dedicated site.

### What this enables for FinOps and procurement

The FinOps site is the most immediately useful for an under-served audience. FinOps practitioners and procurement teams are the people who most need machine-readable cost-and-billing-model data across vendors, and they've historically been served by spreadsheets compiled by hand. With FOCUS v1.3 columns indexed across 3,786 providers, comparing two providers' FinOps shape is now a query, not a research project.

The Plans and Rate Limits sites are the most immediately useful for integrators evaluating which provider to build against. Pricing transparency at the index level — "here are nine providers in this category, here's what each one charges, here are their rate ceilings" — is the kind of comparison that has historically required a half-day of portal-spelunking per evaluation. It's now a filter on plans.apis.io.

### How they're built

Same pipeline as the rest of the network. The [`network/scripts/build.py`](https://github.com/api-search/network/blob/main/scripts/build.py) script reads each provider's `plans/`, `rate-limits/`, and `finops/` directories from the upstream [api-evangelist](https://github.com/api-evangelist) repos and emits one Markdown file per source YAML into the corresponding collection. Each site is its own Jekyll deploy on GitHub Pages — independent build, independent collection, shared chrome and navigation.

The new sites follow the same conventions as the rest of the network: filterable browse on the homepage, per-provider detail pages with breadcrumbs back to the provider profile, source YAML embedded in a widget on every detail page, RFC 9727 and CNAME wiring inherited from the network template.

Reconciliation work continues. The scaffolded 3,372 documents will close as we work through the catalog provider-by-provider, and reconciled counts will move into the network update posts as new providers come online.

For now: [plans.apis.io](https://plans.apis.io), [rate-limits.apis.io](https://rate-limits.apis.io), [finops.apis.io](https://finops.apis.io). Three new entry points into the network, one for each of the three operational dimensions that didn't previously have a home.
