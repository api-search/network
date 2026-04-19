---
description: A data integration flow definition
layout: schema
name: DataIntegrationFlow
properties_list:
- description: The instance identifier
  name: instanceId
  type: string
- description: The flow name
  name: name
  type: string
- description: Data sources for the flow
  name: sources
  type: array
- description: Data transformation configuration
  name: transformation
  type: object
- description: Data target configuration
  name: target
  type: object
- description: Creation timestamp
  name: createdTime
  type: string
- description: Last modification timestamp
  name: lastModifiedTime
  type: string
provider_name: Amazon Supply Chain
provider_slug: amazon-supply-chain
schema_file: json-schema/amazon-supply-chain-data-integration-flow-schema.json
slug: amazon-supply-chain-data-integration-flow
tags:
- AWS
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
title: DataIntegrationFlow
---
