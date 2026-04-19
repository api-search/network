---
description: SourcePatchRequest schema from Airbyte API
layout: schema
name: SourcePatchRequest
properties_list:
- description: ''
  name: name
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
schema_file: json-schema/airbyte-source-patch-request-schema.json
slug: airbyte-source-patch-request
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: SourcePatchRequest
---
