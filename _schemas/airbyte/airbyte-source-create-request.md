---
description: SourceCreateRequest schema from Airbyte API
layout: schema
name: SourceCreateRequest
properties_list:
- description: Name of the source e.g. dev-mysql-instance.
  name: name
  type: string
- description: The UUID of the connector definition. One of configuration.sourceType or definitionId must be provided.
  name: definitionId
  type: string
- description: ''
  name: workspaceId
  type: string
- description: ''
  name: configuration
  type: object
- description: Optional secretID obtained through the OAuth redirect flow.
  name: secretId
  type: string
- description: ''
  name: resourceAllocation
  type: object
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-source-create-request-schema.json
slug: airbyte-source-create-request
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: SourceCreateRequest
---
