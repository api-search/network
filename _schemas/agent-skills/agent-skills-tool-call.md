---
description: An AI agent's invocation of a tool skill with specific input parameters.
layout: schema
name: ToolCall
properties_list:
- description: Unique identifier for this tool call instance.
  name: id
  type: string
- description: Content block type, always tool_use.
  name: type
  type: string
- description: Name of the tool being called.
  name: name
  type: string
- description: Input parameters provided to the tool, conforming to the tool's input_schema.
  name: input
  type: object
provider_name: Agent Skills
provider_slug: agent-skills
schema_file: json-schema/agent-skills-tool-call-schema.json
slug: agent-skills-tool-call
tags:
- Agent Skills
- AI Agents
- Tool Use
- Function Calling
- MCP
- Agentic AI
- Automation
title: ToolCall
---
