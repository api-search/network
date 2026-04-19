---
class_count: 5
classes:
- QueryDataRequest
- QueryDataResponse
- CreateSessionRequest
- CreateSessionResponse
- QueryDocumentRequest
context_file: json-ld/agentql-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agentql/refs/heads/main/json-ld/agentql-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agentql from AgentQL.
layout: jsonld
name: Agentql Context
namespaces:
- prefix: agql
  uri: https://api.agentql.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: url
  type: reference
- container: ''
  name: query
  type: string
- container: ''
  name: prompt
  type: string
- container: ''
  name: html
  type: string
- container: ''
  name: data
  type: reference
- container: ''
  name: metadata
  type: reference
- container: ''
  name: requestId
  type: string
- container: ''
  name: responseTimeMs
  type: integer
- container: ''
  name: sessionId
  type: string
- container: ''
  name: cdpUrl
  type: reference
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: mode
  type: string
- container: ''
  name: waitFor
  type: integer
- container: ''
  name: browserProfile
  type: string
- container: ''
  name: browserUaPreset
  type: string
- container: ''
  name: inactivityTimeoutSeconds
  type: integer
property_count: 16
provider_name: AgentQL
provider_slug: agentql
slug: agentql-context
tags:
- Agents
- Artificial Intelligence
- Web Scraping
- Data Extraction
- Browser Automation
- REST API
- JSON-LD
- Linked Data
- Semantic Web
---
