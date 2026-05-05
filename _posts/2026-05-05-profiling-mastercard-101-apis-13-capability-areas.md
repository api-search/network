---
date: 2026-05-05
image: /assets/images/blog/profiling-mastercard-101-apis-13-capability-areas.png
layout: post
tags:
- Mastercard
- Payments
- Open Banking
- Fraud Prevention
- Capabilities
- Provider Profile
title: Profiling Mastercard — 101 APIs Across 13 Capability Areas
---


When you think of payments APIs, the names that come up first are usually the modern fintech entrants — Stripe, Plaid, Adyen. The card networks that move the actual money tend to sit one layer beneath that conversation. But [Mastercard's developer surface](https://developer.mastercard.com/) is one of the largest and most thoroughly partitioned API catalogs of any payments provider, and it's now fully indexed at [providers.apis.io/providers/mastercard](https://providers.apis.io/providers/mastercard/).

The Mastercard profile in the catalog covers **101 APIs**, organized into **13 distinct capability areas**, with **20 JSON-LD context documents** describing the entities those APIs manipulate. It's a useful example of what a fully-built-out enterprise API surface looks like when you stop thinking about "the payments API" and start thinking about all the things a payment network actually does.

### The 13 capability areas

Each Mastercard capability is a Naftiko spec that composes several APIs into a workflow for a specific persona. The thirteen capability areas in the catalog map to the operational domains of a global card network:

**[Payment Processing and Checkout](https://capabilities.apis.io/capabilities/mastercard-payment-processing-and-checkout/)** is the core authorization and capture surface most developers think of first. **[Card and Account Management](https://capabilities.apis.io/capabilities/mastercard-card-and-account-management/)** handles issuer-side operations — lifecycle, controls, and account services. **[Money Transfer and Disbursements](https://capabilities.apis.io/capabilities/mastercard-money-transfer-and-disbursements/)** covers Mastercard Send and the cross-border push-payment surface.

**[Fraud Prevention and Risk](https://capabilities.apis.io/capabilities/mastercard-fraud-prevention-and-risk/)** composes the fraud database, Ethoca alerts, merchant screening (MATCH), and onboarding risk checks into a single workflow for fraud analysts. **[Identity and Authentication](https://capabilities.apis.io/capabilities/mastercard-identity-and-authentication/)** covers 3D Secure, EMV, and identity verification. **[Digital Enablement and Tokenization](https://capabilities.apis.io/capabilities/mastercard-digital-enablement-and-tokenization/)** is the wallet-and-token layer — MDES, Click to Pay, and the supporting cryptography APIs.

**[Open Banking and Data Analytics](https://capabilities.apis.io/capabilities/mastercard-open-banking-and-data/)** wraps the consumer-permissioned data and credit analytics platform Mastercard built around Finicity. **[Disputes and Settlement](https://capabilities.apis.io/capabilities/mastercard-disputes-and-settlement/)** handles chargeback workflows. **[Bill Payments and Commercial](https://capabilities.apis.io/capabilities/mastercard-bill-payments-and-commercial/)** covers Bill Pay Exchange and the B2B commercial surface.

**[Loyalty and Offers](https://capabilities.apis.io/capabilities/mastercard-loyalty-and-offers/)**, **[Merchant Services and Locations](https://capabilities.apis.io/capabilities/mastercard-merchant-services-and-locations/)**, and **[Community Pass and Inclusion](https://capabilities.apis.io/capabilities/mastercard-community-pass-and-inclusion/)** round out the consumer- and merchant-facing services. The thirteenth capability is **[Sustainability](https://capabilities.apis.io/capabilities/mastercard-sustainability/)** — Mastercard's Carbon Calculator and the Doconomy Åland Index integration that lets cardholders see the carbon footprint of their spending.

That last one is worth pausing on. A capability description for "calculate the carbon footprint of cardholder spending" sitting next to "process a payment authorization" is exactly the right shape for an API catalog in 2026. The same network that moves money is increasingly being asked to surface the environmental cost of that money moving.

### What the surface looks like up close

Each of the 101 APIs in the Mastercard profile carries a thorough property set. Pulling a sample API entry from the catalog shows what's there:

- **Documentation, Getting Started, Use Cases, Tutorials and Guides** — the operational developer-experience surface
- **OpenAPI specifications** — machine-readable contracts for every endpoint
- **Authentication, Security, Rate Limits, Error Codes, Status Page** — the production-readiness checklist
- **Sandbox, Release Notes, Change Log, Versioning, Glossary, FAQ** — the integration-lifecycle surface
- **SDK, Code Examples, API Reference** — the implementation surface

This is what a complete APIs.json entry looks like when an organization treats their developer surface as a product. Twenty different property types per API, all machine-readable, all linkable from an index, all indexable by something like the APIs.io network. (We'll write more about the apis.yml file structure itself in [a follow-up post on the apis.json blog](https://apisjson.org/blog/).)

### Why the capability framing matters

A list of 101 APIs is hard to use. "Find me the right Mastercard API for handling chargebacks" is not a question someone unfamiliar with the catalog can answer by browsing endpoint names. The capability layer does the work of grouping APIs into the workflows a real persona — fraud analyst, issuer engineer, merchant integrator, ESG team — would actually run.

[Disputes and Settlement](https://capabilities.apis.io/capabilities/mastercard-disputes-and-settlement/) doesn't surface as one API; it's a workflow that consumes several APIs together. [Open Banking](https://capabilities.apis.io/capabilities/mastercard-open-banking-and-data/) consumes Open Banking Solutions, Consumer Credit Analytics, and the supporting permission and consent APIs. The capability is what an integrator would actually deploy, expressed in business language.

### The takeaway

Mastercard isn't usually the example people reach for when they're talking about modern API design — that conversation tends to centre on smaller, opinionated providers with a tighter surface. But a payments network with 101 APIs, organized into thirteen capability domains, with 20 property types per API and a sustainability capability sitting next to payment authorization, is exactly the shape of a 2026 enterprise API catalog.

For anyone building against Mastercard, or thinking about how to organize a comparable enterprise API portfolio, the [Mastercard profile on APIs.io](https://providers.apis.io/providers/mastercard/) is now a usable index — and the capability links above are a cleaner entry point than starting from the developer portal homepage.
