---
class_count: 7
classes:
- Tool
- ToolCall
- ToolResult
- MCPServer
- name
- description
- version
context_file: json-ld/agent-skills-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-ld/agent-skills-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agent Skills from Agent Skills.
layout: jsonld
name: Agent Skills Context
namespaces:
- prefix: ask
  uri: https://api-evangelist.github.io/agent-skills/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: type
  type: string
- container: ''
  name: inputSchema
  type: reference
- container: ''
  name: input
  type: reference
- container: ''
  name: strict
  type: boolean
- container: ''
  name: id
  type: string
- container: ''
  name: toolUseId
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: isError
  type: boolean
- container: ''
  name: transport
  type: string
- container: set
  name: tools
  type: reference
- container: set
  name: resources
  type: reference
- container: set
  name: prompts
  type: reference
- container: ''
  name: uri
  type: reference
- container: ''
  name: mimeType
  type: string
- container: set
  name: required
  type: string
- container: ''
  name: properties
  type: reference
property_count: 16
provider_name: Agent Skills
provider_slug: agent-skills
slug: agent-skills-context
tags:
- Agent Skills
- AI Agents
- Tool Use
- Function Calling
- MCP
- Agentic AI
- Automation
- JSON-LD
- Linked Data
- Semantic Web
---
