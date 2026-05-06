---
date: 2026-05-06
image: /assets/images/blog/2136-capabilities-on-apis-io-and-running-them-with-naftiko.png
layout: post
tags:
- Capabilities
- Naftiko
- MCP
- REST
- Agent Skills
- Spec-Driven Integration
title: 2,136 Capabilities on APIs.io and How to Run Them With the Naftiko Framework
---


The capabilities count on [capabilities.apis.io](https://capabilities.apis.io) crossed **2,136 capabilities** in this morning's rebuild — a +767 jump from yesterday. That number deserves more than a stats-bump update because each of those capabilities isn't just a description; it's a YAML spec that an open-source framework can run as a live REST API, an MCP server, and an agent skill, all from the same file.

This post walks through what's in the catalog, how the capabilities are organized, and how to take any one of them and run it locally with [Naftiko](https://github.com/naftiko/framework).

### What's in the 2,136

Every capability in the catalog is a [Naftiko capability spec](https://github.com/naftiko/framework/wiki/Specification) — a YAML file with three sections:

**`info:`** describes the capability in business language. Not "the AccuWeather API" but "AccuWeather Weather Intelligence" — a workflow scoped to a specific persona (developers building weather-aware applications). The label, description, and tags answer "what can this *do for someone*," not "what HTTP verbs does this expose."

**`consumes:`** is the import list. Each capability composes one or more APIs into a single workflow. The [1Password Secrets Management capability](https://capabilities.apis.io/capabilities/1password-secrets-management/) consumes the Connect Server API, the Events API, and the Partnership API. The [Mastercard Open Banking capability](https://capabilities.apis.io/capabilities/mastercard-open-banking-and-data/) consumes Open Banking Solutions, Consumer Credit Analytics, and the supporting permission and consent APIs. The composition layer is what an integrator would otherwise have to write themselves.

**`exposes:`** is where the capability becomes deployable. Across the 2,136 capabilities in the catalog, the spread of expose types looks like this:

- **2,273 MCP servers** — capabilities that expose themselves as named tools to AI agents
- **2,246 REST APIs** — clean HTTP surfaces for traditional application integration
- **227 Agent Skills** — capabilities packaged as `SKILL.md` artifacts for IDE-resident assistants

Most capabilities ship at least two surfaces (REST + MCP) from the same spec. A growing slice — currently 227 — also ship an agent skill as a third surface. Three protocols, one YAML file, one set of credentials.

### How the catalog is organized

The 2,136 capabilities are tagged into **26 cross-provider categories**, which is what [capabilities.apis.io/categories](https://capabilities.apis.io/categories/) renders. The distribution gives a useful read on where the API ecosystem's actual workflow density is:

- **[Analytics](https://capabilities.apis.io/categories/analytics/)** — 27 capabilities
- **[Monitoring](https://capabilities.apis.io/categories/monitoring/)** — 23 capabilities
- **[Security](https://capabilities.apis.io/categories/security/)** — 17 capabilities
- **[Automation](https://capabilities.apis.io/categories/automation/)** — 16 capabilities
- **[Data Engineering](https://capabilities.apis.io/categories/data-engineering/)**, **[Messaging](https://capabilities.apis.io/categories/messaging/)** — 14 each
- **[Procurement & Supply Chain](https://capabilities.apis.io/categories/procurement-supply-chain/)** — 13 capabilities
- **[Container Orchestration](https://capabilities.apis.io/categories/container-orchestration/)**, **[Identity & Access](https://capabilities.apis.io/categories/identity-access/)**, **[Compliance](https://capabilities.apis.io/categories/compliance/)**, **[Payments](https://capabilities.apis.io/categories/payments/)** — 12 each
- **[Content Management](https://capabilities.apis.io/categories/content-management/)**, **[IoT](https://capabilities.apis.io/categories/iot/)** — 11 each
- **[API Management](https://capabilities.apis.io/categories/api-management/)**, **[Machine Learning](https://capabilities.apis.io/categories/machine-learning/)** — 10 each

Plus CRM, incident management, payroll/HR, collaboration, customer engagement, CI/CD, object storage, serverless, recruiting, document processing, and travel booking. Twenty-six clean entry points into the catalog by what someone is actually trying to *do*, rather than by which vendor they happen to be looking at.

### Running a capability with Naftiko

The capability YAML in the catalog isn't documentation. It's an executable spec. Pick any capability page on [capabilities.apis.io](https://capabilities.apis.io), download the YAML, and the [Naftiko framework](https://github.com/naftiko/framework) will run it as a live multi-protocol service.

The framework engine ships as a Docker image (and an optional CLI for authoring). Per the [official installation guide](https://github.com/naftiko/framework/wiki/Installation), the shortest path from a capability page to a running surface looks like this:

```bash
# Pull the Naftiko engine image
docker pull ghcr.io/naftiko/naftiko-framework:v1.0.0-alpha2

# Pull a capability YAML — pick one from capabilities.apis.io
curl -O https://raw.githubusercontent.com/api-evangelist/1password/main/capabilities/1password-secrets-management.yaml

# Run the engine, mounting the capability as a volume.
# Forward the port the capability's `exposes:` block declares.
docker run -p 8081:3001 \
  -v $(pwd)/1password-secrets-management.yaml:/app/test.capability.yaml \
  -e CONNECT_TOKEN=... -e EVENTS_TOKEN=... -e PARTNERSHIP_TOKEN=... \
  ghcr.io/naftiko/naftiko-framework:v1.0.0-alpha2 /app/test.capability.yaml
```

A couple of practical notes from the install docs: if the capability's `consumes:` block points at a service running on your local machine, use `host.docker.internal` rather than `localhost` (the engine runs in an isolated container). And if the capability `exposes:` itself locally, bind the listener to `0.0.0.0` rather than `localhost` so requests forwarded from outside the container reach it.

What that command gives you, all at once, is whatever surfaces the capability declares — the REST API on the forwarded port, an MCP server addressable by Claude, Copilot, or any other MCP client, and (if the spec includes a `type: skill` block) an agent skill ready for IDE consumption. Three protocols from a single docker run and a single YAML file.

The optional [Naftiko CLI](https://github.com/naftiko/framework/wiki/Installation#naftiko-cli) is a separate tool — installed via `curl` and `chmod` — that helps you scaffold and validate capability YAML before you run it (`naftiko create capability`, `naftiko validate <file>`), and it can also bootstrap a Naftiko `consumes` adapter directly from an existing OpenAPI document with `naftiko import openapi <file>`. Useful if you're authoring new capabilities, not strictly required to run the ones already in the catalog.

### Running fleets, not just specs

The framework runs one capability at a time. [Naftiko Fleet](https://github.com/naftiko/fleet) is the governed runtime that runs many at once — discoverable through an inventory, composable across domains, observable through OpenTelemetry, and cost-bounded through policy controls. Fleet is offered as a Community Edition (freeware) and ships with a VS Code extension for editing capabilities and Backstage templates for cataloguing them.

For most individual developers, the framework alone is enough — pull a capability, set the env vars, run it, point Claude at the MCP endpoint. For platform teams running dozens of capabilities across an organization, Fleet is the layer that makes that operationally manageable.

### Why this scales the way it does

The reason the catalog can be 2,136 capabilities deep is that the capability spec is small enough to write quickly and complete enough to run as-is. The same YAML file describes how to authenticate, what APIs to consume, what data transformations to apply, what surfaces to expose, and what credentials to bind to — all in one validated artifact that lives in Git.

Each capability in the catalog represents work that an integrator would otherwise have to do themselves: read the API docs, figure out how to authenticate, figure out which calls to compose, figure out what schema to expose, figure out how to ship it as both an HTTP service and an MCP server. The spec collapses all of that into a single YAML file and a single command.

That's the practical claim of the catalog: 2,136 pieces of integration work that an organization no longer has to do from scratch. Find the capability, fork the YAML, swap in your credentials, run it. From the catalog page to a running multi-protocol service is roughly a five-minute path.

For the index of all 2,136 capabilities, [capabilities.apis.io](https://capabilities.apis.io) has a filterable browse. For the framework that runs them, [github.com/naftiko/framework](https://github.com/naftiko/framework). For the runtime that orchestrates fleets of them, [github.com/naftiko/fleet](https://github.com/naftiko/fleet).
