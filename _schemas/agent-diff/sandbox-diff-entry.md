---
description: DiffEntry schema from Agent Diff API
layout: schema
name: DiffEntry
properties_list:
- description: Unique diff identifier.
  name: id
  type: string
- description: Sandbox that produced this diff.
  name: sandbox_id
  type: string
- description: API operation that triggered the state change.
  name: operation
  type: string
- description: When the operation occurred.
  name: timestamp
  type: string
- description: ''
  name: changes
  type: array
provider_name: Agent Diff
provider_slug: agent-diff
schema_file: json-schema/sandbox-diff-entry-schema.json
slug: sandbox-diff-entry
tags:
- API Testing
- AI Agents
- Sandboxing
- API Diffing
- Developer Tools
title: DiffEntry
---
