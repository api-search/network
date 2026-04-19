---
description: A Model Context Protocol server that exposes agent skills (tools, resources, prompts) to AI clients.
layout: schema
name: MCPServer
properties_list:
- description: Name of the MCP server.
  name: name
  type: string
- description: Server version.
  name: version
  type: string
- description: Communication transport used by the server.
  name: transport
  type: string
- description: List of tools exposed by this MCP server.
  name: tools
  type: array
- description: List of resources (data sources) the server can provide.
  name: resources
  type: array
- description: Reusable prompt templates exposed by the server.
  name: prompts
  type: array
provider_name: Agent Skills
provider_slug: agent-skills
schema_file: json-schema/agent-skills-mcp-server-schema.json
slug: agent-skills-mcp-server
tags:
- Agent Skills
- AI Agents
- Tool Use
- Function Calling
- MCP
- Agentic AI
- Automation
title: MCPServer
---
