---
date: '2026-05-11'
image: /assets/images/blog/agent-frameworks-roundup.png
layout: post
tags:
- Agent Frameworks
- Agent SDKs
- Bedrock AgentCore
- Microsoft Agent Framework
- Roundup
title: 'The Runtime Below MCP: 15 Stories on Agent Frameworks and SDKs From One Week'
---


# The Runtime Below MCP: 15 Stories on Agent Frameworks and SDKs From One Week

Below the MCP surface and the skill bundle, there is a runtime layer — agent frameworks, agent SDKs, agent gateways, and the orchestration primitives that hold the whole stack together. The week of May 4-8, 2026 produced 15 stories about that runtime layer across the API Evangelist network. AWS Bedrock AgentCore, Microsoft Agent Framework, and a long tail of vendor-specific agent SDKs are all converging on a similar shape, and the competitive landscape underneath agentic AI is starting to crystallize.

This roundup organizes the week into four themes — the cloud-platform agent runtimes, the framework-and-SDK launches from independent vendors, the orchestration and handoff patterns, and the meta-question of which framework an organization should pick.

## 1. Cloud Platform Agent Runtimes

The hyperscalers are racing to ship the runtime layer.

- **[AWS](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/)** — _Agents that transact: Introducing Amazon Bedrock AgentCore payments, built with Coinbase and Stripe._ Payments primitive inside AgentCore, with Coinbase and Stripe as launch partners. Agents that move money is a meaningful threshold.
- **[AWS](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-amazon-bedrock-agentcore-identity-on-amazon-ecs/)** — _Secure AI agents with Amazon Bedrock AgentCore Identity on Amazon ECS._ Identity inside the runtime, ECS-native.
- **[AWS](https://aws.amazon.com/blogs/machine-learning/introducing-os-level-actions-in-amazon-bedrock-agentcore-browser/)** — _Introducing OS Level Actions in Amazon Bedrock AgentCore Browser._ Browser-control primitives inside AgentCore. AWS is filling out the runtime in primitives — payments, identity, browser, OS-level actions — at a fast pace.
- **[Microsoft](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/)** — _Microsoft Agent Framework – Building Blocks for AI Part 3._ Microsoft's .NET-native agent framework continues its content series.
- **[Microsoft](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)** — _Durable Workflows in the Microsoft Agent Framework._ Durable execution as a primitive in the agent runtime — the right shape for any non-trivial agent workflow.

## 2. Framework and SDK Launches

The independents are publishing in the same direction with different framings.

- **[Twilio](https://www.twilio.com/en-us/blog/products/launches/agent-connect)** — _What is Twilio Agent Connect? Meet the model-agnostic bridge between your AI agents and real customers._ Twilio's framing of an agent runtime that talks to humans across communication channels.
- **[Twilio](https://www.twilio.com/en-us/blog/developers/tutorials/integrations/ai-twilio-agent-connect-amazon-bedrock-agentcore)** — _Build an Omni-Channel AI Agent with Twilio Agent Connect and Amazon Bedrock AgentCore._ Twilio + AgentCore reference implementation.
- **[Airbyte](https://airbyte.com/blog/agent-sdk)** — _The Airbyte Agent SDK: Ship Agents, Not Data Plumbing._ Data-vendor agent SDK.
- **[Solo.io](https://www.solo.io/blog/inbound-auth-for-agentcore-with-agentgateway)** — _Inbound Auth for Agentcore With Agentgateway._ Gateway pattern for agent runtimes.
- **[ScrapingBee](https://www.scrapingbee.com/blog/qwen-agent-framework/)** — _Your Guide to Qwen-Agent: Build Powerful AI Agents with Tools & RAG._ Qwen-Agent primer for the non-OpenAI / non-Anthropic agent stack.

## 3. Orchestration and Handoff Patterns

Two pieces this week pointed at the same problem space — what happens at the boundary between agents, and between agents and humans.

- **[Twilio](https://www.twilio.com/en-us/blog/developers/best-practices/ai-human-handoff-tac-orchestrator-studio-flex)** — _Orchestrate an AI-to-Human Agent Handoff with Twilio Agent Connect, Conversations Orchestrator, Studio, and Flex._ The AI-to-human handoff problem, with Twilio's full stack for solving it.
- **[n8n](https://blog.n8n.io/ai-agent-architecture-patterns/)** — _AI Agent Architecture Patterns: From Prototype To Production._ Architecture patterns for agent systems — orchestration, memory, error handling — the practical engineering work.
- **[SignOz](https://signoz.io/docs/claude-agent-monitoring)** — _Claude Agent SDK Monitoring & Observability with OpenTelemetry._ Observability for the Claude Agent SDK runtime.

## 4. Vendor Comparisons and the Meta Question

When a market reaches enough launches, the comparison content starts arriving.

- **[Apify](https://blog.apify.com/best-ai-agent-frameworks/)** — _11 best AI agent frameworks and platforms._ The expected listicle, useful for a market scan.
- **[American Express](https://americanexpress.io/trust-without-disclosure-why-zero-knowledge-proofs-could-help-build-trust-in-ai-agents/)** — _Trust Without Disclosure: Why Zero-Knowledge Proofs Could Help Build Trust in AI Agents._ Forward-looking piece on the trust primitive — relevant for any framework that claims agent-attestability.

## What This Signals For the Network

Three takeaways from this week's agent-runtime coverage:

1. **The runtime layer is becoming a contested platform space.** AWS Bedrock AgentCore is shipping primitives faster than any independent framework can match. Microsoft Agent Framework is the .NET-native counter-bet. The independents (n8n, Airbyte, Twilio) are positioning around verticals or specific concerns (orchestration, data, communications). Selecting an agent framework in 2026 is a real strategic decision.
2. **Agents that transact is the threshold that just got crossed.** AWS shipping AgentCore Payments with Coinbase and Stripe means the next wave of agentic systems will move money. The implications for governance, fraud, and credential scoping are large.
3. **Durable execution and orchestration are becoming first-class.** Microsoft Agent Framework durable workflows, Twilio's AI-to-human handoff orchestration, and n8n's architecture patterns all point at the same conclusion — the agent runtime needs to handle long-running, multi-step, sometimes-failing workflows reliably. The frameworks that get this right will be the survivors.

We are tracking the agent runtime layer of every provider in the api-evangelist network on apis.io. If you are publishing agent frameworks, SDKs, or runtime primitives we should know — [apis.io](https://apis.io/) is where we index the operational surface of the API economy.

