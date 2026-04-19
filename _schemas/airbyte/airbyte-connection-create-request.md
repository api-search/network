---
description: ConnectionCreateRequest schema from Airbyte API
layout: schema
name: ConnectionCreateRequest
properties_list:
- description: Optional name of the connection
  name: name
  type: string
- description: ''
  name: sourceId
  type: string
- description: ''
  name: destinationId
  type: string
- description: ''
  name: configurations
  type: object
- description: ''
  name: schedule
  type: object
- description: ''
  name: dataResidency
  type: string
- description: ''
  name: namespaceDefinition
  type: object
- description: Used when namespaceDefinition is 'custom_format'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
  name: namespaceFormat
  type: string
- description: Prefix that will be prepended to the name of each stream when it is written to the destination (ex. “airbyte_” causes “projects” => “airbyte_projects”).
  name: prefix
  type: string
- description: ''
  name: nonBreakingSchemaUpdatesBehavior
  type: object
- description: ''
  name: status
  type: object
- description: ''
  name: tags
  type: array
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-connection-create-request-schema.json
slug: airbyte-connection-create-request
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: ConnectionCreateRequest
---
