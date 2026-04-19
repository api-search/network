---
description: DestinationCreateRequest schema from Airbyte API
layout: schema
name: DestinationCreateRequest
properties_list:
- description: Name of the destination e.g. dev-mysql-instance.
  name: name
  type: string
- description: The UUID of the connector definition. One of configuration.destinationType or definitionId must be provided.
  name: definitionId
  type: string
- description: ''
  name: workspaceId
  type: string
- description: ''
  name: configuration
  type: object
- description: ''
  name: resourceAllocation
  type: object
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-destination-create-request-schema.json
slug: airbyte-destination-create-request
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: DestinationCreateRequest
---
