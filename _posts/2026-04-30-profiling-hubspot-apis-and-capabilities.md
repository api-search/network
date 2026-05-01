---
image: /assets/images/blog/profiling-hubspot-apis-and-capabilities.png
layout: post
tags:
- Provider Profile
- HubSpot
- CRM
- Marketing
- Commerce
- Capabilities
- MCP
title: Profiling HubSpot's 63 APIs and 11 Capabilities
---


HubSpot is one of the wider provider profiles in the APIs.io catalog — wider than most because the platform has grown well past its CRM origins and now spans marketing, content, commerce, customer service, and a developer platform with its own primitives. The [HubSpot profile](https://github.com/api-search/hubspot) currently catalogs **63 APIs** described in [apis.yml](https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/apis.yml), with **26 of them carrying machine-readable OpenAPI definitions** and **11 capability bundles** describing how those APIs combine into something an agent can actually run.

This post walks through what's in there.

## The APIs, grouped by what they do

Naming the 63 individually would be a wall of bullet points. The shape is clearer when grouped by the surface they touch:

- **CRM core** — Contacts, Companies, Deals, Tickets, Pipelines, Products, Line Items, Quotes, Owners, Custom Objects, plus the cross-cutting Properties, Associations, Imports, Lists, and Search APIs. This is the heart of HubSpot and the most fully profiled section of the catalog.
- **Sales engagement** — Calls, Emails, Meetings, Notes, Tasks, plus the Calling Extensions API for embedding telephony.
- **Marketing** — Marketing Email, Marketing Events, Forms, Subscriptions, Campaigns, Analytics Events, plus Custom Workflow Actions for Operations Hub automation.
- **Content / CMS** — Domains, Source Code, Posts, Authors, URL Redirects, Blog Tags, CMS Pages, CMS HubDB, CMS Site Search, CMS Content Audit.
- **Commerce** — Carts, Commerce Payments, Commerce Subscriptions, plus the line-item and quote primitives shared with CRM.
- **Customer service & conversations** — Conversations, Tickets, Feedback Submissions.
- **Developer platform** — OAuth, Webhooks, Business Units, Account Information, CRM Feature Flags, plus the Public Apps and Private Apps surfaces.

That coverage is the reason HubSpot lands in nearly every canonical capability bucket the [`capabilities.apis.io/categories/`](https://capabilities.apis.io/categories/) aggregator carries — `crm`, `marketing-automation`, `payments`, `email`, `forms`, `cms`, `analytics`, `webhooks`. One provider, ten or so canonical categories.

## From APIs to capabilities

The 26 OpenAPI definitions are the ingredient list. The interesting part is the [capabilities directory](https://github.com/api-search/hubspot/tree/main/capabilities), where individual APIs are bundled into named workflows that consume multiple specs and re-expose them as a single agent-facing surface:

| Capability | Consumed APIs | Exposed Tools |
|---|---|---|
| `crm-management` | 7 (Contacts, Companies, Deals, Tickets, Associations, Search, Lists) | 71 |
| `content-management` | 6 (Domains, Source Code, Posts, Authors, URL Redirects, HubDB) | 63 |
| `sales-engagement` | 5 (Calls, Emails, Meetings, Notes, Tasks) | 58 |
| `automation-and-integration` | 4 | 40 |
| `commerce-operations` | 2 (Payments, Subscriptions) | 20 |
| `marketing-automation` | 2 | 8 |
| `commerce-admin`, `content-and-marketing`, `customer-service`, `developer-platform`, `sales-pipeline` | — | placeholders |

The populated capabilities expose between 8 and 71 named tools each, every one tagged with `readOnly: true` for safe reads or `destructive: true` for archive/delete operations — the same hint surface that drives MCP tool gating today and will drive whatever the agent runtime expects tomorrow. The unpopulated ones are honest placeholders: the API list is staked out, the bundling work hasn't shipped yet.

## What an MCP-native CRM bundle looks like

`crm-management.yaml` is the most fleshed-out of the bunch and worth a closer look. It declares one MCP server on port 9090, binds the single `HUBSPOT_ACCESS_TOKEN` env var, and exposes 71 tools — `listcontacts`, `createcontact`, `searchcompanies`, `batchcreatedeals`, `deleteticket`, `addlistmembers`, and so on across all four CRM object types plus the Associations, Search, and Lists APIs. The destructive operations (`deletecontact`, `deletedealassociation`, `deleteassociationlabel`) carry the `destructive: true` hint; everything safe carries `readOnly: true`.

That's the difference between cataloging seven OpenAPI specs and shipping one capability: the capability is the bundle an agent runs. It says *"to manage CRM in HubSpot, here are the seven APIs you need, here's the env binding they share, here are the 71 actions exposed as a single MCP server, and here's which ones are safe to call without confirmation."* That's a layer above the API description and a layer below the agent itself — and it's the layer the catalog is now built to carry.

## Where the gaps are

Profiling is never finished. A few honest gaps in the HubSpot profile as of this snapshot:

- **37 of 63 APIs have no OpenAPI yet** — they're catalogued from the human docs but don't have a machine-readable description that an agent can call. Many of these are HubSpot's older or more niche APIs (Calling Extensions, Business Units, Marketing Events) where HubSpot itself doesn't publish a public OpenAPI; closing the gap requires sourcing or generating the spec.
- **5 of 11 capabilities are placeholders** — `commerce-admin`, `content-and-marketing`, `customer-service`, `developer-platform`, and `sales-pipeline` have the directory entry and intent but no `consumes:` or `exposes:` block yet. The naming is deliberate so the bundles can be filled in without renaming downstream.
- **The Custom Objects API** is in the apis.yml but doesn't yet flow into a capability — it's the right primitive to underpin a "flexible CRM" capability that the current `crm-management` bundle deliberately doesn't cover, since custom objects need per-tenant property discovery before the tool list can be statically declared.

These show up in the catalog as APIs without `service-desc` links and as capabilities without exposed tools, so they're filterable rather than hidden.

## Why HubSpot is a useful profile to study

HubSpot sits at a sweet spot for the catalog. It's big enough to exercise every layer — apis.json indexing, OpenAPI ingestion, capability bundling, MCP tool exposure, canonical-category cross-classification — but small enough that the whole profile is comprehensible in one read. Compared to AWS-style providers with 100+ services and shallow capability metadata, HubSpot has fewer APIs but the bundling work has gone deeper: the capabilities aren't just a tag cloud, they're runnable.

If you want to see what a fully-profiled provider looks like end-to-end — apis.yml at the top, OpenAPI per API, JSON Schema and JSON Structure per response shape, capability YAML bundling APIs into MCP servers, canonical-category classification linking it across providers — [the HubSpot directory](https://github.com/api-search/hubspot) is the cleanest reference in the network right now.

The provider page at [`providers.apis.io/providers/hubspot/`](https://providers.apis.io/providers/hubspot/) is the entry point. Hit it with `Accept: text/markdown` to get the agent-readable view; the [api-catalog linkset](https://providers.apis.io/.well-known/api-catalog) carries every machine-readable link in the profile.