---
date: '2026-05-22'
image: /assets/images/blog/api-roundup.png
layout: post
tags:
- APIs
- REST
- GraphQL
- OpenAPI
- SDK
- API Security
- Roundup
title: 'Just APIs: 30 Stories From One Week That Are Not About MCP, Skills, or CLIs'
---


# Just APIs: 30 Stories From One Week That Are Not About MCP, Skills, or CLIs

It is easy this year to read every API story through the lens of MCP, skills, and the agent surface. Useful as that lens is, it can hide what is happening at the foundational layer — the actual REST endpoints, OpenAPI specs, SDKs, gateways, credentials, and documentation that make up the API economy. The week of May 4-8, 2026 produced 30 stories worth tracking that have nothing directly to do with MCP, agent skills, or AI-coding CLIs. Those 30 stories tell a different and equally important story about where the foundation is moving.

This roundup organizes them into six themes — API keys and credentials, API specs and documentation, GraphQL and federation, API management and gateways, API quality and testing, and the SDK launches that landed this week.

## 1. API Keys and Credentials Are Getting Real Attention

Zuplo published an entire week of API key content, and HubSpot dropped a careful piece on credential type selection. Combined with the Truto and DORA-compliance work, this is a category that is finally getting the systematic treatment it deserved a decade ago.

- **[Zuplo](https://zuplo.com//blog/introducing-apikeys-guide)** — _The Missing Manual for API Keys._ The flagship piece of the week's content series.
- **[Zuplo](https://zuplo.com//blog/api-key-best-practices)** — _API Key Best Practices for 2026._ Reasonable, practical, current.
- **[Zuplo](https://zuplo.com//blog/add-self-serve-api-keys-to-your-own-app)** — _Add Self-Serve API Keys to Your Own App._
- **[Zuplo](https://zuplo.com//blog/provision-api-keys-at-first-login)** — _Provision API Keys at First Login._ The auto-provisioning UX pattern that quietly improves first-touch developer experience for every API.
- **[Zuplo](https://zuplo.com//blog/using-jwt-and-api-key-auth-on-the-same-route)** — _Using JWT and API Key Auth on the Same Route._
- **[Zuplo](https://zuplo.com//blog/api-key-week-wrap-up)** — _API Key Week Wrap Up._ The summary post.
- **[HubSpot](https://developers.hubspot.com/blog/hubspot-service-keys-the-right-api-credential-for-data-integrations)** — _HubSpot Service Keys: The Right API Credential for Data Integrations._ HubSpot doing the work of explaining which credential type to use for which integration pattern, with documentation that says when not to use each one.
- **[Truto](https://truto.one/blog/how-to-manage-third-party-api-quotas-across-internal-microservices/)** — _How to Manage Third-Party API Quotas Across Microservices at Scale._
- **[Truto](https://truto.one/blog/how-to-manage-third-party-api-risk-for-dora-compliance-in-the-eu-financial-sector/)** — _How to Manage Third-Party API Risk for DORA Compliance in EU Finance (2026)._
- **[Auth0](https://auth0.com/blog/secure-spring-boot-api-with-auth0/)** — _Secure Your Spring Boot API with Auth0 in Minutes._

What stands out: when a category is healthy, you see a single vendor (Zuplo here) doing a content series, an established platform (HubSpot) shipping the deeper conceptual piece, and operational guidance (Truto) framing the cross-cutting concern. All three patterns happened in the same week.

## 2. API Specs and Documentation Are Quietly Getting Better

The unsexy work of shipping cleaner specs and better-housed documentation continues, and it matters.

- **[Cisco / Webex](https://developer.webex.com/blog/webex-postman-collection-reaches-ga-plus-new-openapi-specs-repository)** — _Webex Postman Collection Reaches GA Plus New OpenAPI Specs Repository._ Postman collection plus an OpenAPI specs repo, both as first-class artifacts. The right shape.
- **[WooCommerce](https://developer.woocommerce.com/2026/05/08/new-woo-rest-api-docs/)** — _WooCommerce REST API docs have a new home._ Documentation rehoming is the kind of housekeeping that signals a vendor is investing in the developer relationship.
- **[Microsoft 365 Dev](https://devblogs.microsoft.com/microsoft365dev/announcing-general-availability-of-the-mailbox-import-and-export-microsoft-graph-apis/)** — _Announcing general availability of the mailbox import and export Microsoft Graph APIs._ Graph API GA, useful capability.
- **[Microsoft Power BI](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Execute-DAX-Queries-REST-API-Preview/ba-p/5177697)** — _Execute DAX Queries REST API (Preview)._ Programmatic DAX is exactly the kind of capability that turns a tool into a platform.
- **[Zuplo](https://zuplo.com//blog/flask-api-tutorial)** — _How to Build a Production-Ready Flask REST API in 2026._ Tutorial work for a current developer cohort.
- **[DreamFactory](https://blog.dreamfactory.com/8-api-documentation-examples)** — _The 8 Best API Documentation Examples._ Curation of good examples is how the floor of documentation quality rises across the industry.
- **[APIMatic](https://www.apimatic.io/blog/april-2026-product-highlights)** — _April '26 Highlights: Add Custom Code to SDKs, Create API Portals Using AI Agents, and Publish SDKs From the APIMatic CLI._

## 3. GraphQL and Federation Make a Move

One headline-grabbing GraphQL story this week:

- **[Apollo](https://www.apollographql.com/blog/apollo-federation-goes-full-rust)** — _Apollo Federation Goes Full Rust._ Rewriting Federation in Rust is a meaningful infrastructure move — performance, memory profile, and cross-language embeddability all change at the same time. Worth tracking the migration story over the next quarter to see whether the rewrite ships smoothly.

## 4. API Management and Gateways Keep Reshuffling

The API management space is in motion, with incumbents stepping back and new patterns emerging:

- **[DreamFactory](https://blog.dreamfactory.com/is-oracle-api-gateway-reaching-the-end-of-the-road-what-to-do-next)** — _Is Oracle API Gateway Reaching the End of the Road? What to Do Next._ The "the incumbent is dying" post is a reliable signal of an inflection point in a category.
- **[DreamFactory](https://blog.dreamfactory.com/beyond-api-management-with-dreamfactory)** — _Beyond API management with DreamFactory._ Same vendor staking out the next-generation framing.
- **[DreamFactory](https://blog.dreamfactory.com/multi-version-api-management-for-ai-workflows)** — _Multi-Version API Management for AI Workflows._ Versioning specifically for AI workflows is going to be a real category. Different versions for different agent contexts; rolling deprecations that respect agent-side caches.
- **[NGINX](https://blog.nginx.org/blog/nginx-gateway-fabric-2-6-f5-waf-for-nginx-comes-to-the-gateway-api)** — _NGINX Gateway Fabric 2.6: F5 WAF for NGINX Comes to the Gateway API._ Kubernetes Gateway API maturity continues; WAF integration raises the floor on production deployments.
- **[Perforce / Akana](https://www.perforce.com/resources/aka/api-ops)** — _Streamline API Management with Akana API Ops._ API ops as a category framing for the discipline of managing APIs at scale.

## 5. API Quality and Testing Keeps Getting Better

Quality and testing tooling is a slow-and-steady part of the API economy that does not get the headlines but matters every day:

- **[MuleSoft](https://blogs.mulesoft.com/artificial-intelligence/how-ai-transforms-api-quality/)** — _Intelligent Assurance: How AI Transforms API Quality._ AI-assisted quality assurance is going to be a category — every API testing vendor will ship a version of this within twelve months.
- **[Harness](https://www.harness.io/blog/api-security-testing-just-got-easier-smarter)** — _API Testing Enhancements: Easier Setup, Smarter Scans._
- **[Kreya](https://kreya.app/blog/testing-rest-apis/)** — _Testing REST APIs with Kreya._ Tooling space that rewards the underrated.
- **[Truto](https://truto.one/blog/how-to-handle-long-running-saas-api-tasks-in-ai-agent-tool-calling-workflows/)** — _How to Handle Long-Running SaaS API Tasks in AI Agent Workflows._ The long-running-task problem in agent contexts is exactly the kind of operational issue that does not have a clean solution yet.

## 6. SDK Launches and Updates That Landed

The SDK side of the API economy keeps shipping. A representative slice of this week:

- **[Vonage](https://developer.vonage.com/en/blog/introducing-audio-connector-sdk-and-pipecat-serializer-for-ai-audio-apis)** — _Introducing Audio Connector SDK & Pipecat Serializer for AI Audio Apps._ Audio is a fast-moving category and Vonage is shipping the SDKs to ride it.
- **[Airbyte](https://airbyte.com/blog/agent-sdk)** — _The Airbyte Agent SDK: Ship Agents, Not Data Plumbing._ Agent-flavored SDKs from data integration vendors will keep showing up — Airbyte's framing is the right one.
- **[Autodesk](https://aps.autodesk.com/blog/secure-service-account-sdks-now-beta-net-and-typescript)** — _Secure Service Account SDKs now in Beta: .NET and TypeScript._ Service-account auth in SDK form is the right pattern for machine-to-machine integrations.
- **[AWS](https://aws.amazon.com/blogs/developer/announcing-the-general-availability-of-amazon-s3-transfer-manager-for-swift/)** — _Announcing AWS SDK for Swift's Transfer Manager for Amazon S3._
- **[Sentry](https://blog.sentry.io/debugging-expo-react-native-sdk/)** — _Improved debugging for Expo apps with the React Native SDK._
- **[Nutrient](https://www.nutrient.io/blog/sdk-product-updates-q1-2026/)** — _Nutrient SDK product updates for Q1 2026._
- **[OpenAI](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api)** — _Advancing voice intelligence with new models in the API._
- **[Google Workspace](http://workspaceupdates.googleblog.com/feeds/3472145267365863334/comments/default)** — _Now generally available: Bulk import using client-side encryption and the Drive API._
- **[Anthropic / Finout](https://www.finout.io/blog/anthropics-enterprise-analytics)** — _Anthropic's Enterprise Analytics API: Per-User AI Cost Attribution Is Finally Here._ Cost attribution at the per-user level is one of the most-requested AI-API features, and Anthropic landing it is a small but real shift.
- **[EODHD](https://eodhd.com/financial-apis-blog/exchange-details-api-v2-is-live)** — _Exchange Details API v2 is live._

## What This Signals For the Network

Three takeaways from a week of "just API" stories:

1. **The credentials story is finally getting the systematic treatment it has needed.** Zuplo's API key week, HubSpot Service Keys, Auth0 Spring Boot, and the Truto third-party API risk pieces all in one week is the strongest "this category is healthy now" signal we have seen in a while. Combined with the agent-identity work covered in [the broader newsletter](2026-05-07-weekly-api-evangelist-draft-v2.md), it suggests credentials are about to become the most-discussed API operational concern of 2026.
2. **API management is mid-restructure, with old incumbents fading and AI-aware management arriving.** The Oracle Gateway "end of the road" post, DreamFactory's multi-version-for-AI piece, and the NGINX Gateway WAF all point in the same direction.
3. **The SDK + spec + docs trio is quietly improving in parallel with the agent surface.** The vendors paying attention to all three layers (Cisco's Postman + OpenAPI repo, APIMatic publishing SDKs from a CLI, Autodesk shipping Secure Service Account SDKs in beta) are positioning well for whatever the agent ecosystem looks like in 2027.

The foundation matters even when the headlines are about MCP, skills, and agent CLIs. We are tracking all of these signals — credentials, specs, gateways, SDKs, quality tooling — across every provider in the api-evangelist network on apis.io. If you ship API tooling we should know — [apis.io](https://apis.io/) is where we index the API economy at its actual surface.

