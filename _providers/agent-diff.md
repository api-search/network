---
api_count: 1
apis:
- description: Create and manage isolated, ephemeral sandbox replicas of third-party APIs. Run AI agents against sandboxes to produce deterministic state-change diffs without rate limits or side effects.
  name: Agent Diff Sandbox API
  slug: agent-diff-sandbox-api
capabilities:
- description: ''
  name: Api Agent Testing
  slug: api-agent-testing
common:
- title: ''
  type: Portal
  url: https://www.agentdiff.dev/
- title: ''
  type: GettingStarted
  url: https://www.agentdiff.dev/docs
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/rules/agent-diff-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/capabilities/api-agent-testing.yaml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/capabilities/shared/agent-diff-sandbox-api.yaml
- title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/json-schema/agent-diff-sandbox-sandbox-schema.json
- title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/json-schema/agent-diff-sandbox-diff-entry-schema.json
- title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/json-ld/agent-diff-sandbox-context.jsonld
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/vocabulary/agent-diff-vocabulary.yaml
created: '2026-01-02'
description: Agent Diff creates isolated, ephemeral replicas of third-party APIs (Slack, Linear, GitHub). Agents interact with these sandboxes to produce deterministic state-change diffs without side effects, rate limits, or real API calls. Ideal for testing AI agents that interact with external APIs.
features: []
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations: []
jsonld:
- class_count: 6
  name: Agent Diff Sandbox Context
  property_count: 15
  slug: agent-diff-sandbox-context
layout: provider
modified: '2026-04-19'
name: Agent Diff
rules:
- name: Agent Diff API Rules
  rule_count: 24
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 10
  slug: agent-diff-spectral-rules
skills: []
slug: agent-diff
solutions: []
tags:
- API Testing
- AI Agents
- Sandboxing
- API Diffing
- Developer Tools
url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/apis.yml
use_cases: []
---
