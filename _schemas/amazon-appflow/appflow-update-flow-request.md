---
description: UpdateFlowRequest schema from Amazon AppFlow API
layout: schema
name: UpdateFlowRequest
properties_list:
- description: The specified name of the flow.
  name: flowName
  type: string
- description: Idempotency token.
  name: clientToken
  type: string
- description: A description of the flow.
  name: description
  type: string
- description: ''
  name: triggerConfig
  type: object
- description: ''
  name: sourceFlowConfig
  type: object
- description: ''
  name: destinationFlowConfigList
  type: array
- description: ''
  name: tasks
  type: array
- description: ''
  name: metadataCatalogConfig
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-update-flow-request-schema.json
slug: appflow-update-flow-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: UpdateFlowRequest
---
