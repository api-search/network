---
description: Compatibility record showing which AI tools support a given .aiignore syntax
layout: schema
name: AIToolCompatibility
properties_list:
- description: Name of the AI coding tool
  name: tool_name
  type: string
- description: The actual ignore file name this tool uses
  name: file_name
  type: string
- description: Ignore file syntax type
  name: syntax
  type: string
- description: Where file should be placed
  name: scope
  type: string
- description: Link to tool documentation
  name: documentation_url
  type: string
provider_name: .AIIgnore
provider_slug: aiignore
schema_file: json-schema/aiignore-ai-tool-compatibility-schema.json
slug: aiignore-ai-tool-compatibility
tags:
- AI Agents
- Configuration
- Developer Workflow
- Security
- Privacy
- Developer Tools
- LLM
- Secrets Management
title: AIToolCompatibility
---
