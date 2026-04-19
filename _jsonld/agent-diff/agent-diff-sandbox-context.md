---
class_count: 6
classes:
- DiffEntry
- Sandbox
- createdAt
- SandboxCreateRequest
- DiffList
- SandboxList
context_file: json-ld/agent-diff-sandbox-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/json-ld/agent-diff-sandbox-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agent Diff Sandbox from Agent Diff.
layout: jsonld
name: Agent Diff Sandbox Context
namespaces:
- prefix: agent-diff
  uri: https://agent-diff.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: sandboxId
  type: string
- container: ''
  name: operation
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: set
  name: changes
  type: reference
- container: ''
  name: api
  type: string
- container: ''
  name: scenario
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: baseUrl
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: seedData
  type: reference
- container: ''
  name: ttl
  type: integer
- container: set
  name: diffs
  type: string
- container: ''
  name: total
  type: integer
- container: set
  name: sandboxes
  type: string
property_count: 15
provider_name: Agent Diff
provider_slug: agent-diff
slug: agent-diff-sandbox-context
tags:
- API Testing
- AI Agents
- Sandboxing
- API Diffing
- Developer Tools
- JSON-LD
- Linked Data
- Semantic Web
---
