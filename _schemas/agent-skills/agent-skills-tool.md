---
description: A skill definition for an AI agent including name, description, and input parameter schema.
layout: schema
name: Tool
properties_list:
- description: The type of tool (custom or provider built-in).
  name: type
  type: string
- description: Unique name of the tool used to identify the invocation.
  name: name
  type: string
- description: Human-readable description of what the tool does, used by the model to decide when to call it.
  name: description
  type: string
- description: JSON Schema defining the parameters the tool accepts.
  name: input_schema
  type: object
- description: When true, enforces strict JSON Schema compliance for tool call inputs.
  name: strict
  type: boolean
provider_name: Agent Skills
provider_slug: agent-skills
schema_file: json-schema/agent-skills-tool-schema.json
slug: agent-skills-tool
tags:
- Agent Skills
- AI Agents
- Tool Use
- Function Calling
- MCP
- Agentic AI
- Automation
title: Tool
---
