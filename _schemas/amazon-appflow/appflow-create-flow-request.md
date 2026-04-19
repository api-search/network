---
description: CreateFlowRequest schema from Amazon AppFlow API
layout: schema
name: CreateFlowRequest
properties_list:
- description: The specified name of the flow. Spaces are not allowed. Use underscores or hyphens only.
  name: flowName
  type: string
- description: Idempotency token to ensure CreateFlow completes only once.
  name: clientToken
  type: string
- description: A description of the flow you want to create.
  name: description
  type: string
- description: The ARN of the KMS key for encryption.
  name: kmsArn
  type: string
- description: ''
  name: metadataCatalogConfig
  type: object
- description: ''
  name: triggerConfig
  type: object
- description: ''
  name: sourceFlowConfig
  type: object
- description: The configuration that controls how Amazon AppFlow places data in the destination connector.
  name: destinationFlowConfigList
  type: array
- description: A list of tasks that Amazon AppFlow performs while transferring data in the flow run.
  name: tasks
  type: array
- description: The tags used to organize, track, or control access for your flow.
  name: tags
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-create-flow-request-schema.json
slug: appflow-create-flow-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: CreateFlowRequest
---
