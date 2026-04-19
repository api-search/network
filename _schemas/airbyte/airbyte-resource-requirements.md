---
description: optional resource requirements to run workers (blank for unbounded allocations)
layout: schema
name: ResourceRequirements
properties_list:
- description: ''
  name: cpu_request
  type: string
- description: ''
  name: cpu_limit
  type: string
- description: ''
  name: memory_request
  type: string
- description: ''
  name: memory_limit
  type: string
- description: ''
  name: ephemeral_storage_request
  type: string
- description: ''
  name: ephemeral_storage_limit
  type: string
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-resource-requirements-schema.json
slug: airbyte-resource-requirements
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: ResourceRequirements
---
