---
description: Sandbox schema from Agent Diff API
layout: schema
name: Sandbox
properties_list:
- description: Unique sandbox identifier.
  name: id
  type: string
- description: The third-party API being sandboxed.
  name: api
  type: string
- description: Scenario name for this sandbox.
  name: scenario
  type: string
- description: Current sandbox status.
  name: status
  type: string
- description: Base URL for interacting with the sandbox replica.
  name: base_url
  type: string
- description: When the sandbox was created.
  name: created_at
  type: string
- description: When the sandbox will expire.
  name: expires_at
  type: string
provider_name: Agent Diff
provider_slug: agent-diff
schema_file: json-schema/sandbox-sandbox-schema.json
slug: sandbox-sandbox
tags:
- API Testing
- AI Agents
- Sandboxing
- API Diffing
- Developer Tools
title: Sandbox
---
