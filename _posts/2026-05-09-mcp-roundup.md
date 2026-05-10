---
date: '2026-05-09'
image: /assets/images/blog/mcp-roundup.png
layout: post
tags:
- MCP
- Model Context Protocol
- Agent Skills
- API Discovery
- Roundup
title: 'The MCP Surface, Mapped: 31 Stories From One Week'
---


# The MCP Surface, Mapped: 31 Stories From One Week

The week of May 4-8, 2026 produced 31 distinct stories across the API Evangelist network about Model Context Protocol — vendors shipping servers, building gateways, writing how-to guides, hardening the auth and testing layers, and curating "best of" lists. That is a third of the API-keyword-relevant volume for the week in one topic. A year ago MCP was an emerging idea. Today it is the surface that vendors with serious developer ambitions are actively shipping into.

We use apis.io to keep track of where the API economy is moving. This week the answer is loud: it is moving toward MCP, and the shape of that movement matters more than the volume.

This roundup organizes the week's MCP-related publications into five themes — the new MCP servers shipping, the how-to ecosystem expanding around them, the infrastructure (auth, testing, multi-tenancy) maturing underneath, the meta-layer of curation and education forming on top, and the open questions still in front of all of it.

## 1. New MCP Servers Shipped This Week

The most-watched signal each week is which providers shipped a fresh MCP server. Eight launches this week, ranging from broad SaaS to specialized infrastructure:

- **[Twilio](https://www.twilio.com/en-us/blog/developers/introducing-twilio-mcp-skills)** — _Introducing the Twilio MCP Server and Skills: Give Your Coding Agents Native Access to 1,800+ Twilio APIs._ Twilio paired the MCP server with a curated skills bundle, the strongest example this week of shipping the protocol and the agent guidance together rather than separately.
- **[Quarkus](https://quarkus.io/blog/introducing-agent-mcp/)** — _Introducing Quarkus Agent MCP: teaching AI agents to speak Quarkus._ A framework-native MCP, scoped to the Quarkus runtime — the first wave of language- and framework-specific MCPs is starting to arrive.
- **[Optimizely](https://www.optimizely.com/insights/blog/experimentation-mcp-server/)** — _Remote MCP Server is here: Bring Optimizely into your AI tools._ Experimentation tooling becomes agent-consumable, which makes sense — feature flags and experiment lifecycles are exactly the kind of read-mostly surface MCP fits cleanly.
- **[Port](https://www.port.io/blog/integrate-software-catalog-every-workflow-port-mcp-server)** — _Integrate Your Catalog: Port MCP Server Launch._ Internal developer platform → MCP. The IDP space is rapidly becoming a leading consumer of MCP because the catalog is what an agent needs to navigate any organization's services.
- **[Airbyte](https://airbyte.com/blog/agent-mcp)** — _The Airbyte MCP: One Connection, Your Entire Business Context._ Data integration provider exposing connectors as MCP tools — the value proposition writes itself for agents that need cross-system context.
- **[Finout](https://www.finout.io/blog/introducing-finouts-mcp-integration)** — _Introducing Finout's MCP Integration._ FinOps as MCP. Cost data is naturally read-mostly, which makes it a clean fit.
- **[Databricks](https://www.databricks.com/blog/mcp-marketplace-brings-real-time-intelligence-agentic-applications)** — _MCP Marketplace Brings Real-Time Intelligence to Agentic Applications._ Not a single server but a marketplace, signaling the shift from individual MCP launches to MCP distribution as its own product category.
- **[SingleStore](https://www.singlestore.com/blog/building-an-ai-database-assistant-with-singlestore-and-mcp-toolbox-for-databases)** — _Building an AI Database Assistant with SingleStore and MCP Toolbox for Databases._ Database vendor pairing with the Google MCP Toolbox to ship a curated agent surface.

What stands out: Twilio's bundle of MCP + Skills is the right shape, Databricks moving to a marketplace model is the leading indicator that we are about to see MCP servers traded as packages, and the framework-native MCPs (Quarkus) suggest the next twelve months will see one MCP per major runtime.

## 2. The How-To Ecosystem Filling Out

When a layer becomes a default, the how-to content explodes. This week saw a measurable quick-connector cluster, mostly from integration platforms targeting Claude Code as the consumer:

- **[Merge](https://www.merge.dev/blog/freshdesk-mcp-claude-code)** — _How to connect a Freshdesk MCP with Claude Code (4 steps)._
- **[Merge](https://www.merge.dev/blog/expensify-mcp-claude-code)** — _How to connect an Expensify MCP with Claude Code (4 steps)._
- **[Merge](https://www.merge.dev/blog/coda-mcp-claude-code)** — _How to connect a Coda MCP with Claude Code (4 steps)._
- **[Merge](https://www.merge.dev/blog/calendly-mcp-claude-code)** — _How to connect a Calendly MCP with Claude Code (4 steps)._
- **[Merge](https://www.merge.dev/blog/zoom-mcp-claude-code)** — _How to connect a Zoom MCP with Claude Code (4 steps)._
- **[Document360](https://document360.com/blog/chatgpt-mcp-knowledge-base-integration/)** — _Connect ChatGPT to Your Knowledge Base with MCP: A Practical Guide._
- **[Unified.to](https://unified.to/blog/how_to_get_started_with_a_workday_mcp_server)** — _How to Get Started with a Workday MCP Server._
- **[ZoomInfo](https://pipeline.zoominfo.com/sales/perplexity-zoominfo-mcp)** — _Use Perplexity to Find Verified Contacts and Company Data with ZoomInfo._

The Merge cluster is interesting on its own — five vendor-specific MCP-with-Claude-Code recipes in one week, each scoped to a SaaS that already has a Merge connector. The play is clear: integration platforms are positioning themselves as the connective tissue between agent harnesses (Claude Code, Cursor, Codex) and the SaaS catalog. The "X MCP with Claude Code in 4 steps" template is going to be a content workhorse for integration vendors for the rest of the year.

## 3. The Infrastructure Layer Is Maturing

Underneath the launches and the how-tos, the infrastructure that determines whether MCP can run safely at scale is getting serious work this week:

- **[Auth0](https://auth0.com/blog/auth0-auth-for-mcp-servers-generally-available/)** — _Auth for MCP Is Now Generally Available._ This is the most consequential MCP infrastructure announcement of the week. Auth0 moving from preview to GA on MCP auth means a lot of the "we shipped an MCP server" stories from earlier in the year now have a path to production-grade authentication.
- **[Truto](https://truto.one/blog/how-to-test-and-mock-mcp-servers-in-cicd-without-hitting-live-apis/)** — _How to Test and Mock MCP Servers in CI/CD Without Hitting Live APIs._ CI/CD harnesses for MCP have arrived — a strong "this layer has graduated" signal.
- **[Truto](https://truto.one/blog/how-to-architect-a-multi-tenant-mcp-server-for-enterprise-b2b-saas/)** — _How to Architect a Multi-Tenant MCP Server for Enterprise B2B SaaS._ Multi-tenancy is the next architectural problem after auth. Truto is publishing on it before most vendors have even started thinking about it.
- **[Tyk](https://tyk.io/blog/imagine-build-share-how-integration-testing-led-me-to-create-the-tyk-mock-mcp-server/)** — _Imagine, build, share — how integration testing led me to create the Tyk mock MCP server._ Mock MCP servers as a primitive for development and CI testing.

The pattern: auth → CI/CD test harness → mock runtime → multi-tenant architecture. That is the same maturity arc every successful API protocol has gone through. We are seeing it compressed into months instead of years for MCP.

## 4. Curation, Education, and the Meta-Layer

Once an ecosystem reaches enough volume, the meta-layer arrives — best-of lists, hackathons, marketplaces, education content for newcomers:

- **[Stack Overflow Blog](https://stackoverflow.blog/2026/05/08/no-dumb-questions-mcp/)** — _No Dumb Questions: What is an MCP server and why do I care?_ Stack Overflow taking the time to write the explainer is a leading indicator that the long tail of developers is finally encountering MCP and asking what it is.
- **[PostHog](https://posthog.com/blog/best-mcp-servers-for-startups)** — _The best MCP servers for developers at startups._ The "best of" listicle has arrived.
- **[Solo.io](https://www.solo.io/blog/celebrating-the-winners-of-the-2026-hackathon-for-mcp-ai-agents)** — _Celebrating the Winners of the 2026 Hackathon for MCP & AI Agents._ Hackathons as ecosystem-formation infrastructure.
- **[Databricks](https://www.databricks.com/blog/mcp-marketplace-brings-real-time-intelligence-agentic-applications)** — The MCP Marketplace mentioned earlier doubles as a curation surface, distributing curated MCP packages.
- **[Amplitude](https://amplitude.com/blog/mcp-bug-investigation)** — _Agents Write Code. Fixing It Is Still On You._ A more skeptical, more grounded piece — the agents are productive, but they still leave bugs behind, and someone has to investigate. Worth reading in tandem with the upbeat launches.
- **[DZone](https://dzone.com/articles/model-context-protocol-mcp-for-nl2sql-a-rigorous-e)** — _Custom Model Context Protocol (MCP) for NL2SQL: A Rigorous Evaluation Framework on Oracle Database._ Empirical evaluation rather than launch hype — exactly what the discourse needs more of.

## 5. The Open Questions in Front of It All

Two pieces this week pose the questions the community has not answered yet:

- **[API Evangelist](https://apievangelist.com/blog/2026/05/07/seeing-mcp/)** — _Seeing MCP._ The fundamental question is one of visibility: governance and operations cannot move forward until organizations can see the MCP surface they are exposing — what tools are published, who can call them, with what credentials, on whose behalf.
- **[Amplitude](https://amplitude.com/blog/mcp-bug-investigation)** — _Agents Write Code. Fixing It Is Still On You._ Honest framing about the residual human work after agent productivity gains.

The unresolved questions — discovery, governance, attestation, deprecation, credential scoping — are the same shape as the questions APIs have had for fifteen years, applied to a layer that is moving faster than we have ever seen.

## What This Signals For the Network

Looking at one week of MCP coverage across the api-evangelist network, three patterns are worth tracking:

1. **MCP servers are no longer optional for vendors with developer ambitions.** Eight launches in one week from across the SaaS, data, framework, and IDP categories. Any vendor whose customers use Claude Code, Cursor, or Codex is now expected to ship an MCP surface.
2. **The Merge / integration-platform play is maturing into a content engine.** "How to connect X MCP with Claude Code in 4 steps" is going to be the dominant form of integration-platform content for the rest of 2026.
3. **The infrastructure layer (auth, testing, multi-tenancy, marketplaces) graduated this week.** Auth0 GA + Truto CI/CD + Tyk mock + Databricks marketplace is the four-corner foundation that turns MCP from "we shipped one" to "we run them in production safely."

We are tracking the MCP surface of every provider in the api-evangelist network on apis.io. If you ship an MCP server we should know about — or you want to find which providers in our index ship one — that is the work we do at [apis.io](https://apis.io/).

