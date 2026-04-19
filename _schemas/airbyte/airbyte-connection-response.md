---
description: Provides details of a single connection.
layout: schema
name: ConnectionResponse
properties_list:
- description: ''
  name: connectionId
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: sourceId
  type: string
- description: ''
  name: destinationId
  type: string
- description: ''
  name: workspaceId
  type: string
- description: ''
  name: status
  type: object
- description: ''
  name: schedule
  type: object
- description: ''
  name: nonBreakingSchemaUpdatesBehavior
  type: object
- description: ''
  name: namespaceDefinition
  type: object
- description: ''
  name: namespaceFormat
  type: string
- description: ''
  name: prefix
  type: string
- description: ''
  name: configurations
  type: object
- description: ''
  name: createdAt
  type: integer
- description: ''
  name: tags
  type: array
- description: ''
  name: statusReason
  type: string
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-connection-response-schema.json
slug: airbyte-connection-response
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: ConnectionResponse
---
