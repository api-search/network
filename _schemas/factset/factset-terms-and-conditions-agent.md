---
description: Agent Data Items for a Fixed Income security.
layout: schema
name: agent
properties_list:
- description: Security identifier used in the request.
  name: requestId
  type: string
- description: FactSet Permanent Security Identifier.
  name: fsymId
  type: string
- description: FactSet Entity Identifier for the Agent.
  name: agentEntityId
  type: string
- description: Agent Commitment Amount
  name: agentCommAmt
  type: number
- description: Agent Name
  name: agentName
  type: string
- description: Role of the agent
  name: agentType
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-terms-and-conditions-agent-schema.json
slug: factset-terms-and-conditions-agent
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: agent
---
