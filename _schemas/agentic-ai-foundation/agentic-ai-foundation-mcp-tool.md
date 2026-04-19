---
description: An MCP tool definition exposed by an MCP server, discoverable by AI agent clients.
layout: schema
name: MCPTool
properties_list:
- description: Unique name of the tool.
  name: name
  type: string
- description: Human-readable description of what the tool does.
  name: description
  type: string
- description: JSON Schema defining the tool's input parameters.
  name: inputSchema
  type: object
- description: Optional metadata annotations for the tool.
  name: annotations
  type: object
provider_name: Agentic AI Foundation
provider_slug: agentic-ai-foundation
schema_file: json-schema/agentic-ai-foundation-mcp-tool-schema.json
slug: agentic-ai-foundation-mcp-tool
tags:
- AI Agents
- Linux Foundation
- Open Source
- Standards
- MCP
- Agentic AI
- Interoperability
title: MCPTool
---
