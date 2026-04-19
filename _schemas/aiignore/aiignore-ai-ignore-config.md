---
description: Full .aiignore configuration file structure for an AI coding tool
layout: schema
name: AIIgnoreConfig
properties_list:
- description: Target AI tool this config applies to
  name: tool
  type: string
- description: AIIgnore spec version
  name: version
  type: string
- description: List of exclusion rules
  name: rules
  type: array
- description: Human-readable description of this config purpose
  name: description
  type: string
provider_name: .AIIgnore
provider_slug: aiignore
schema_file: json-schema/aiignore-ai-ignore-config-schema.json
slug: aiignore-ai-ignore-config
tags:
- AI Agents
- Configuration
- Developer Workflow
- Security
- Privacy
- Developer Tools
- LLM
- Secrets Management
title: AIIgnoreConfig
---
