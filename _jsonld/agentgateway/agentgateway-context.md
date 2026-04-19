---
class_count: 5
classes:
- LLMBackend
- MCPTarget
- Route
- name
- description
context_file: json-ld/agentgateway-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-ld/agentgateway-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agentgateway from AgentGateway.
layout: jsonld
name: Agentgateway Context
namespaces:
- prefix: agw
  uri: https://agentgateway.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: provider
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: alias
  type: string
- container: ''
  name: baseUrl
  type: reference
- container: ''
  name: url
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: authentication
  type: reference
- container: ''
  name: secretRef
  type: string
- container: ''
  name: tokenRef
  type: string
- container: ''
  name: weight
  type: integer
- container: ''
  name: priority
  type: integer
- container: set
  name: tools
  type: string
- container: set
  name: allowedClients
  type: string
- container: ''
  name: backend
  type: string
- container: set
  name: matches
  type: reference
- container: ''
  name: rateLimit
  type: reference
- container: ''
  name: retries
  type: reference
- container: ''
  name: requestsPerSecond
  type: integer
- container: ''
  name: burstSize
  type: integer
- container: ''
  name: attempts
  type: integer
- container: ''
  name: perTryTimeout
  type: string
property_count: 21
provider_name: AgentGateway
provider_slug: agentgateway
slug: agentgateway-context
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
- JSON-LD
- Linked Data
- Semantic Web
---
