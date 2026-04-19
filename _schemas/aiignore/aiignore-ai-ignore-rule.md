---
description: A single .aiignore exclusion rule pattern with metadata
layout: schema
name: AIIgnoreRule
properties_list:
- description: Glob pattern for matching files/directories
  name: pattern
  type: string
- description: Human-readable explanation of this rule
  name: comment
  type: string
- description: If true, this rule re-includes a previously excluded path (starts with !)
  name: negated
  type: boolean
- description: 'Scope: file, directory, or pattern'
  name: scope
  type: string
provider_name: .AIIgnore
provider_slug: aiignore
schema_file: json-schema/aiignore-ai-ignore-rule-schema.json
slug: aiignore-ai-ignore-rule
tags:
- AI Agents
- Configuration
- Developer Workflow
- Security
- Privacy
- Developer Tools
- LLM
- Secrets Management
title: AIIgnoreRule
---
