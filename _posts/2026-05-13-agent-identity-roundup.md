---
date: '2026-05-13'
image: /assets/images/blog/agent-identity-roundup.png
layout: post
tags:
- Agent Identity
- Credentials
- OAuth
- Service Accounts
- Roundup
title: 'Agent Identity Is the Next Layer: 11 Stories From One Week'
---


# Agent Identity Is the Next Layer: 11 Stories From One Week

While the discourse has been eating MCP and skills, a quieter story has been forming underneath them: which agent is acting as whom, with what credentials, and on whose behalf. The week of May 4-8, 2026 produced 11 stories across the API Evangelist network about agent identity, scoped credentials, and the auth machinery that determines whether an agent population is safe to run in production.

Identity for agents is not the same problem as API keys for humans. An agent inherits some authority from a user, exercises it autonomously across many tools, and leaves an audit trail that needs to be attestable. Vendors are beginning to publish on this in earnest, and the pattern across this week's coverage is consistent — credentials are getting scoped tighter, identity is getting separated from the human user, and the auth layer for agent runtimes is becoming a first-class infrastructure concern.

## 1. The Conceptual Framing Is Settling In

Two posts this week are the canonical references the rest of the conversation will cite.

- **[Auth0](https://auth0.com/blog/ai-agents-have-two-souls-you-control-only-one/)** — _AI Agents Have Two Souls. You Only Control One._ The most thoughtful framing of agent identity I have read this year. The agent has the user's authority and its own runtime authority — they are different, and conflating them is the source of most of the security failures we are about to see.
- **[Merge](https://www.merge.dev/blog/ai-agent-authentication)** — _A guide to authenticating AI agents._ Workmanlike practical guide that names the auth patterns vendors are landing on.

## 2. Vendor Patterns and Practical Tooling

Vendors are publishing on the credential management problem, the scoped-token problem, and the runtime-identity problem in parallel.

- **[1Password](https://1password.com/blog/credential-management-for-ai-agents)** — _Credential management for AI agents._ The credential vault vendors are pivoting their narrative toward agent-held credentials. 1Password is positioning early.
- **[HubSpot](https://developers.hubspot.com/blog/hubspot-service-keys-the-right-api-credential-for-data-integrations)** — _HubSpot Service Keys: The Right API Credential for Data Integrations._ Service keys vs other credential types — the documentation shipping the discriminator is the right work.
- **[GitLab](https://about.gitlab.com/blog/fine-grained-pats/)** — _Limit credential exposure with fine-grained personal access tokens._ Fine-grained PATs are the same shape as scoped agent tokens; the convergence is going to be loud.
- **[HashiCorp](https://www.hashicorp.com/blog/mitigate-credential-exposure-in-windows-environments-with-boundary-and-vault)** — _Mitigate credential exposure in Windows environments with Boundary and Vault._ Boundary + Vault for credential exposure mitigation, with the patterns that are increasingly relevant to agent runtimes.

## 3. Auth Machinery for Agent Runtimes

Auth at the runtime level (not just the user level) is graduating into platform-class infrastructure this week.

- **[AWS](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-amazon-bedrock-agentcore-identity-on-amazon-ecs/)** — _Secure AI agents with Amazon Bedrock AgentCore Identity on Amazon ECS._ AWS shipping AgentCore Identity as part of the Bedrock agent runtime stack. ECS-native scoped identity for agents is the pattern enterprise customers will adopt fastest.
- **[Solo.io](https://www.solo.io/blog/inbound-auth-for-agentcore-with-agentgateway)** — _Inbound Auth for Agentcore With Agentgateway._ Gateway-pattern auth in front of agent runtimes — the same shape as API gateways, scoped to agent traffic.
- **[Cerbos](https://cerbos.dev/blog/iiw42-recap-agent-authorization-got-real)** — _IIW42 recap: Where agent authorization got real._ The Internet Identity Workshop recap shows how the broader identity community is treating agent authorization as a first-class problem now.

## 4. The Frontier: Zero-Knowledge and Supply Chain

Two stories pointing at where the identity story is heading next:

- **[American Express](https://americanexpress.io/trust-without-disclosure-why-zero-knowledge-proofs-could-help-build-trust-in-ai-agents/)** — _Trust Without Disclosure: Why Zero-Knowledge Proofs Could Help Build Trust in AI Agents._ ZKPs as a primitive for proving agent properties without disclosing identity. AmEx publishing on this signals it is moving from research-paper territory toward enterprise viability.
- **[Nudge Security](https://www.nudgesecurity.com/post/how-to-use-nudge-security-to-minimize-risk-from-supply-chain-breaches-like-vercel)** — _How to use Nudge Security to minimize supply chain breach risk._ Supply chain breach detection at the identity layer — relevant when the breach vector is a credential rather than a code change.

## What This Signals For the Network

Three takeaways from this week's agent-identity coverage:

1. **Agent identity is separating from user identity.** Auth0, AWS AgentCore, Cerbos, and the GitLab fine-grained PAT story all point in the same direction — the agent gets its own scoped, attestable identity, distinct from whoever it represents.
2. **The auth runtime is becoming a platform layer.** Bedrock AgentCore Identity on ECS, Solo.io's Agentgateway, and the gateway-pattern auth posts indicate the same architecture pattern as API gateways, applied to agent traffic. The vendors that ship this layer well will end up where the work is.
3. **Credentials need rotation, scoping, and attestation by default.** Every credential-vendor post this week — 1Password, HashiCorp, HubSpot, GitLab — is moving the same direction: shorter-lived, narrower-scoped, audit-friendly credentials as the new default.

We are tracking the agent-identity surface across every provider in the api-evangelist network on apis.io. If you are publishing agent-identity tooling we should know — [apis.io](https://apis.io/) is where we index the operational surface of the API economy.

