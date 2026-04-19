---
description: Configuration for an MCP server target in AgentGateway, defining a connected MCP tool provider.
layout: schema
name: MCPTarget
properties_list:
- description: Unique name for this MCP target.
  name: name
  type: string
- description: The connection type for this MCP target.
  name: type
  type: string
- description: URL of the MCP server endpoint.
  name: url
  type: string
- description: Authentication configuration for connecting to this MCP server.
  name: authentication
  type: object
- description: List of tool names exposed by this MCP target (empty means all tools are available).
  name: tools
  type: array
- description: List of client identifiers permitted to use this MCP target.
  name: allowedClients
  type: array
provider_name: AgentGateway
provider_slug: agentgateway
schema_file: json-schema/agentgateway-mcp-target-schema.json
slug: agentgateway-mcp-target
tags:
- AI Gateway
- API Gateway
- MCP
- LLM
- Agent-to-Agent
- Open Source
- CNCF
- Observability
- Security
title: MCPTarget
---
