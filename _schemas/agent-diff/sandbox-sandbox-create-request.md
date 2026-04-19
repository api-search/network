---
description: SandboxCreateRequest schema from Agent Diff API
layout: schema
name: SandboxCreateRequest
properties_list:
- description: The third-party API to sandbox (e.g., slack, linear, github).
  name: api
  type: string
- description: Named scenario for the sandbox seed data.
  name: scenario
  type: string
- description: Initial state data to populate the sandbox.
  name: seed_data
  type: object
- description: Time-to-live in seconds before the sandbox expires.
  name: ttl
  type: integer
provider_name: Agent Diff
provider_slug: agent-diff
schema_file: json-schema/sandbox-sandbox-create-request-schema.json
slug: sandbox-sandbox-create-request
tags:
- API Testing
- AI Agents
- Sandboxing
- API Diffing
- Developer Tools
title: SandboxCreateRequest
---
