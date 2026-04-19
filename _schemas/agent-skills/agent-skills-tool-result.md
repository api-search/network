---
description: The output returned to an AI agent after executing a tool skill.
layout: schema
name: ToolResult
properties_list:
- description: Content block type, always tool_result.
  name: type
  type: string
- description: The id of the tool_use block this result corresponds to.
  name: tool_use_id
  type: string
- description: The result content returned from the tool. Can be a string or array of content blocks.
  name: content
  type: object
- description: When true, indicates the tool execution returned an error.
  name: is_error
  type: boolean
provider_name: Agent Skills
provider_slug: agent-skills
schema_file: json-schema/agent-skills-tool-result-schema.json
slug: agent-skills-tool-result
tags:
- Agent Skills
- AI Agents
- Tool Use
- Function Calling
- MCP
- Agentic AI
- Automation
title: ToolResult
---
