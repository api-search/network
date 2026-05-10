---
date: '2026-05-10'
image: /assets/images/blog/agent-skills-roundup.png
layout: post
tags:
- Agent Skills
- Claude Skills
- Claude Code
- MCP
- Roundup
title: 'Agent Skills, This Week: 8 Stories From the Layer Above MCP'
---


# Agent Skills, This Week: 8 Stories From the Layer Above MCP

If MCP is the surface that defines what tools exist, **skills** are the layer that defines how to use those tools well. The week of May 4-8, 2026 produced fewer skill-related stories than MCP-related ones (8 vs 31), but the skills coverage carries more weight per post — security incidents, conceptual primers, vendor-bundle launches, and some of the first credible "skills in production" content. The volume gap is itself a signal. The MCP layer is loud because vendors are racing to ship surfaces. The skill layer is quieter because there is real work involved in producing one that does what an agent actually needs.

This roundup organizes the week's skill coverage into four themes — vendor bundles pairing skills with MCP, end-user skill playbooks, the security and supply-chain concerns that are starting to surface, and the conceptual work clarifying what skills even are.

## 1. Vendors Pairing Skills With Their MCP

The strongest pattern this week: vendors that shipped MCP servers are increasingly shipping the skills along with them, in a single bundle.

- **[Twilio](https://www.twilio.com/en-us/blog/developers/introducing-twilio-mcp-skills)** — _Introducing the Twilio MCP Server and Skills: Give Your Coding Agents Native Access to 1,800+ Twilio APIs._ The MCP server is the headline, but the skills bundle is what makes the 1,800-API number tractable for an agent. Without curated skills, an agent has to figure out which of 1,800 tools matters for any given task, which it will not do well.
- **[Twilio](https://www.twilio.com/en-us/blog/partners/introducing-twilio-claude-connector-claude-code-plugin)** — _Twilio Brings Customer Engagement Workflows into Claude by Anthropic._ A second Twilio post the same week, this one a Claude Code plugin packaging customer-engagement workflows. Same vendor, two different flavors of the skill layer — the SDK-level skills bundle and the workflow-level Claude Code plugin.

The Twilio model is going to be widely copied. The MCP server alone is increasingly seen as table stakes. The differentiation — and the sustained engagement — lives in the skill bundle that ships alongside it.

## 2. End-User Skill Playbooks Are Arriving

Skills move from idea to default when end-users start writing about how they use them in real workflows. Three posts this week did exactly that:

- **[Amplitude](https://amplitude.com/blog/5-agent-skills-to-automate-your-weekly-product-review)** — _5 Agent Skills to Automate Your Weekly Product Review._ The product-management workflow is exactly the kind of recurring, multi-tool, judgment-light task that skills are built for. The post reads as a practical playbook, not a marketing piece — five specific skills, each named for the role it plays in the review.
- **[Redpanda](https://www.redpanda.com/blog/claude-code-skills-hooks-frontend)** — _Engineering Den: Claude Code skills and hooks for frontend teams._ Engineering team skill playbook, paired with hooks. The hooks angle is interesting because it puts skill execution into the existing CI/CD lifecycle rather than treating it as a separate ad-hoc activity.
- **[Google Workspace](http://workspaceupdates.googleblog.com/feeds/1156848289397871000/comments/default)** — _Turn your AI prompts into one-click tools using skills in Chrome._ Workspace adding a "skills in Chrome" capability is the consumer-side mirror of the enterprise skill conversation. When the same primitive shows up across Anthropic Claude, Microsoft Copilot, and Google Workspace, you know the abstraction has stuck.

## 3. Skill Security and Supply Chain Concerns Are Surfacing Early

The most consequential skills story this week is a security one:

- **[VentureBeat](https://venturebeat.com/security/anthropic-skill-scanners-passed-every-check-malicious-code-test-file)** — _Anthropic Skill scanners passed every check. The malicious code rode in on a test file._ A skill that passed Anthropic's automated scanners successfully smuggled malicious code via a test file. This is the agent-skill ecosystem's first public supply-chain incident-pattern, and it deserves attention from anyone building infrastructure on top of skills. The skill layer has all the same supply-chain risks as package registries, plus a few that are unique to executable agent context.

Tracking this story matters because skill marketplaces, registries, and distribution mechanisms are forming right now. Whether they form with strong supply-chain controls baked in — provenance attestation, sandboxed execution, behavior monitoring — or whether we replay the npm/PyPI typosquatting era a decade later, depends on what the major skill platforms ship in the next two quarters.

## 4. The Conceptual Layer: What Is a Skill, Anyway?

The other side of the maturity curve — when a layer becomes important enough that vendors start writing primers explaining what it _is_ and how it differs from adjacent concepts:

- **[Relay.app](https://www.relay.app/blog/skills-vs-workflows)** — _Skills vs workflows: What's the difference?_ This is the question every team adopting skills is going to ask. Relay's framing is reasonable — skills are the unit of capability the agent reaches for, workflows are the orchestration that combines them. But the boundary is genuinely fuzzy and we are going to see more of these explainers as different vendors stake out different definitions.
- **[Microsoft](https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/05/copilot-cowork-from-conversation-to-action-across-skills-integrations-and-devices/)** — _Copilot Cowork: From conversation to action across skills, integrations, and devices._ Microsoft framing skills as a first-class layer in their Copilot operational model. The "from conversation to action" framing puts skills at the verb position — they are what turns a Copilot exchange from chat into work. The fact that Microsoft is putting skills, integrations, and devices in the same sentence at the same hierarchy level is a directional bet.

## What This Signals For the Network

Three takeaways from one week of skill coverage:

1. **The skill bundle is becoming the unit of vendor differentiation.** MCP servers are getting commoditized. The skills bundle a vendor ships with their MCP server is increasingly the part that determines whether an agent uses it well or burns through your quota. Twilio is the cleanest current example of this pattern.
2. **Skills are crossing from idea to default workflow.** Amplitude's product-review playbook, Redpanda's frontend playbook, and Google's Chrome skill rollout all suggest skills are starting to land in real, recurring work. The next four quarters will see this accelerate.
3. **The skill supply chain is going to need governance, fast.** The Anthropic skill scanner incident is the first public example of malicious code surviving automated review. Skill marketplaces, attestation, sandboxing, and behavior monitoring need to be on the agenda before the ecosystem is too big to retrofit.

The complementary read is the [MCP roundup](2026-05-08-mcp-roundup-apis-io.md) covering the surface-layer story. Together they describe two halves of the same shift — MCP defines what tools exist, skills define how to use them well, and a healthy agent ecosystem needs both layers maturing in parallel.

We are tracking the skill artifacts shipped by every provider in the api-evangelist network on apis.io. If you are publishing skills alongside your APIs we should know — [apis.io](https://apis.io/) is where we index the agent-consumable surface of the API economy.

