---
description: A pattern category for AI ignore exclusion rules
layout: schema
name: ExclusionPattern
properties_list:
- description: Category name (secrets, proprietary, generated)
  name: category
  type: string
- description: List of glob patterns in this category
  name: patterns
  type: array
- description: Why these files should be excluded
  name: rationale
  type: string
provider_name: .AIIgnore
provider_slug: aiignore
schema_file: json-schema/aiignore-exclusion-pattern-schema.json
slug: aiignore-exclusion-pattern
tags:
- AI Agents
- Configuration
- Developer Workflow
- Security
- Privacy
- Developer Tools
- LLM
- Secrets Management
title: ExclusionPattern
---
