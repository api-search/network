---
image: /assets/images/blog/naftiko-capabilities-apis-mcp-agent-skills.png
layout: post
tags:
- Naftiko
- Capabilities
- MCP
- Agent Skills
- Business Capabilities
- API Design
title: Naftiko Capabilities Turn APIs into Business Workflows That Speak REST, MCP, and Agent Skills
---


The APIs.io catalog now indexes **750 capabilities** across hundreds of providers. That number is easy to scroll past without understanding what it means, because "capability" sounds like a synonym for "API." It isn't. A capability is a layer above the API — a description of what a system can *do* for a specific persona, expressed in business language, and deployable as a REST API, an MCP server, or an agent skill from a single spec. This post explains what Naftiko capabilities are, walks through some of the most interesting ones published to APIs.io, and explains why the expose-type model changes how you think about integrating with APIs in an agent-first world.

## What a Naftiko capability actually is

A capability is a YAML file with three moving parts.

**`info:`** speaks the language of business, not endpoints. The label and description answer "what workflow does this enable and who runs it?" — not "what HTTP verbs does this expose?" The AccuWeather capability is `AccuWeather Weather Intelligence`, not "AccuWeather API wrapper." The 42Crunch capability is `API Security Scanning` scoped to DevSecOps engineers running conformance scans in Kubernetes CI/CD pipelines. The 1Password capability is `1Password Secrets Management` for DevOps engineers and security operations teams. The business context is the primary artifact.

**`capability.consumes:`** is the import list — the individual per-API shared definitions the capability orchestrates. A single capability can pull from several APIs and expose them as a unified surface. The 1Password Secrets Management capability consumes the Connect Server API (vault and item management), the Events API (audit logs and sign-in monitoring), and the Partnership API (account provisioning). HubSpot CRM Management consumes seven APIs — Contacts, Companies, Deals, Tickets, Associations, Search, and Lists. The AccuWeather capability composes location lookup, current conditions, hourly and daily forecasts, minutecast precipitation, air quality, and tropical storm tracking into one workflow. The capability is the composition layer that individual API consumers would otherwise have to write themselves.

**`capability.exposes:`** is where the business capability becomes a deployable interface. This is the part that changes everything.

## One capability, three protocols

Most capabilities in the APIs.io catalog expose two surfaces from the same spec: a REST API and an MCP server. The AccuWeather Weather Intelligence capability declares:

```yaml
exposes:
  - type: rest
    port: 8080
    namespace: weather-intelligence-api
    description: Unified REST API for AccuWeather weather intelligence workflows.
    resources:
      - path: /v1/locations
        ...
      - path: /v1/weather/current/{locationKey}
        ...
      - path: /v1/weather/forecast/hourly/{locationKey}
        ...
      - path: /v1/air-quality/{locationKey}
        ...
      - path: /v1/storms/active/{locationKey}
        ...

  - type: mcp
    port: 9090
    namespace: weather-intelligence-mcp
    transport: http
    description: MCP server for AI-assisted weather intelligence and forecasting workflows.
    tools:
      - name: search-locations
        hints: { readOnly: true, openWorld: true }
        ...
      - name: get-current-weather
        hints: { readOnly: true, openWorld: true }
        ...
      - name: get-air-quality
        hints: { readOnly: true, openWorld: true }
        ...
      - name: get-active-storms
        hints: { readOnly: true, openWorld: true }
        ...
```

The REST surface is for traditional application integration — the AccuWeather API composed into clean HTTP endpoints your application calls. The MCP surface is for agent integration — the same weather intelligence presented as named tools with `readOnly` hints so an AI agent knows which calls are safe to make without confirmation. Both surfaces bind to the same underlying API calls through the same single env var (`ACCUWEATHER_API_KEY`). You write the capability once; [Naftiko](https://github.com/naftiko/fleet) runs it as whichever protocol the consumer needs.

Of the **750 capabilities** currently indexed on APIs.io, **652 expose both REST and MCP** surfaces from the same spec. Twenty expose MCP alone. Zero expose REST alone — which tells you something about where the priority lies in the spec's design.

## MCP hints are first-class design decisions

The MCP surface isn't just a mirror of the REST surface with tools instead of routes. The `hints:` block on each tool is where the capability author communicates safety semantics to the agent runtime:

- `readOnly: true` — safe to call without user confirmation
- `destructive: true` — should prompt before executing  
- `idempotent: true` — safe to retry
- `openWorld: true` — reads from a live external world (weather, search, market data)

The 1Password Secrets Management capability marks `list-vaults`, `list-vault-items`, `get-item`, `get-sign-in-events`, and `get-audit-events` as `readOnly: true`. It marks `delete-item` as `destructive: true, idempotent: true`. It marks `create-item` and `update-item` as `readOnly: false, destructive: false`. These aren't implementation details — they're the capability author's explicit statement about what an agent can do autonomously versus what requires a human in the loop.

HubSpot CRM Management takes this further: 71 tools across 7 CRM APIs, every archive/delete operation flagged `destructive: true`, every read flagged `readOnly: true`. An agent that respects MCP hints can use the entire CRM surface autonomously for reads and searches while surfacing destructive operations for confirmation.

## Business capabilities that cross provider boundaries

The spec doesn't enforce single-provider capabilities. The capability `info.label` and persona description set the frame; the `consumes:` list can pull from any set of shared API definitions. The 42Crunch API Security Scanning capability composes scan management and log retrieval into a DevSecOps workflow that a CI/CD pipeline or a security agent can call. The Atlassian Agile Development capability bundles Jira issues, projects, filters, search, fields, workflows, and dashboards into a workflow built for software developers and scrum masters — not for "people who have read the Jira API docs."

This is the shift the capability layer makes explicit: the API exists at the resource level (this endpoint manages Jira issues), the capability exists at the workflow level (this is how a software team plans and tracks a sprint). The first is for integrators; the second is for agents and the business consumers who orchestrate them.

## Finding capabilities on APIs.io

Every capability published to the catalog is indexed at [`capabilities.apis.io`](https://capabilities.apis.io), organized by canonical category (CRM, monitoring, messaging, payments, and 22 others) at [`capabilities.apis.io/categories/`](https://capabilities.apis.io/categories/). The category aggregator answers the cross-provider question: not "what does AccuWeather expose?" but "which providers offer weather intelligence?" — currently AccuWeather, ClimaCell, AgroMonitoring, OpenWeatherMap, and a handful of others, all mapped to the same canonical category with their capability YAML browsable and runnable from the page.

Each capability page embeds the upstream YAML in the source widget so you can read the full `consumes:` and `exposes:` declaration without leaving the browser. The `Run: Capabilities Using Naftiko` link in every provider README points to the Naftiko fleet runner — the runtime that turns the YAML into a live REST API or MCP server.

The spec version in every file (`naftiko: 1.0.0-alpha1`) is a signal: this is early. The expose-type vocabulary will grow. Agent Skills as a first-class `type:` value is the obvious next addition — a capability that exposes not just REST and MCP but a structured `SKILL.md` consumable by any agent runtime that follows the [agentskills.io](https://agentskills.io) format. The foundation is in place. The 750 capabilities already published are the starting inventory.
