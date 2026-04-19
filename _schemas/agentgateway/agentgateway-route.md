---
description: A routing rule in AgentGateway that matches incoming requests and forwards them to a backend or MCP target.
layout: schema
name: Route
properties_list:
- description: Unique name for this route.
  name: name
  type: string
- description: List of matching criteria for this route.
  name: matches
  type: array
- description: Name of the LLM backend to forward matched requests to.
  name: backend
  type: string
- description: Rate limiting configuration for this route.
  name: rateLimit
  type: object
- description: Retry policy for failed requests.
  name: retries
  type: object
provider_name: AgentGateway
provider_slug: agentgateway
schema_file: json-schema/agentgateway-route-schema.json
slug: agentgateway-route
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
title: Route
---
