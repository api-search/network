---
description: Configuration for an LLM provider backend in AgentGateway, defining the target model, authentication, and routing parameters.
layout: schema
name: LLMBackend
properties_list:
- description: Unique name for this LLM backend.
  name: name
  type: string
- description: The LLM provider for this backend.
  name: provider
  type: string
- description: The model identifier to use for requests.
  name: model
  type: string
- description: Optional alias exposed to clients instead of the actual model name.
  name: alias
  type: string
- description: Base URL for the LLM provider API endpoint.
  name: baseUrl
  type: string
- description: Authentication configuration for this backend.
  name: authentication
  type: object
- description: Load balancing weight for this backend (higher means more traffic).
  name: weight
  type: integer
- description: Failover priority, lower values have higher priority.
  name: priority
  type: integer
provider_name: AgentGateway
provider_slug: agentgateway
schema_file: json-schema/agentgateway-llm-backend-schema.json
slug: agentgateway-llm-backend
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
title: LLMBackend
---
