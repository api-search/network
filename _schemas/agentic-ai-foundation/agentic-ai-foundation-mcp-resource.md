---
description: A data resource exposed by an MCP server, accessible to AI agent clients for reading context.
layout: schema
name: MCPResource
properties_list:
- description: Unique URI identifying this resource.
  name: uri
  type: string
- description: Human-readable name of the resource.
  name: name
  type: string
- description: Human-readable description of the resource's contents.
  name: description
  type: string
- description: MIME type of the resource content.
  name: mimeType
  type: string
- description: Size of the resource in bytes.
  name: size
  type: integer
provider_name: Agentic AI Foundation
provider_slug: agentic-ai-foundation
schema_file: json-schema/agentic-ai-foundation-mcp-resource-schema.json
slug: agentic-ai-foundation-mcp-resource
tags:
- AI Agents
- Linux Foundation
- Open Source
- Standards
- MCP
- Agentic AI
- Interoperability
title: MCPResource
---
