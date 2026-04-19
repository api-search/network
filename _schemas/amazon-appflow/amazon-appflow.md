---
description: Schema defining the structure of an Amazon AppFlow flow resource, including source and destination configurations, task definitions, trigger settings, and flow metadata.
layout: schema
name: Amazon AppFlow Flow Definition
properties_list:
- description: The ARN of the flow.
  name: flowArn
  type: string
- description: The specified name of the flow.
  name: flowName
  type: string
- description: A user-entered description of the flow.
  name: description
  type: string
- description: Indicates the current status of the flow.
  name: flowStatus
  type: string
- description: ''
  name: sourceFlowConfig
  type: object
- description: The configuration that controls how Amazon AppFlow places data in the destination connector.
  name: destinationFlowConfigList
  type: array
- description: A list of tasks that Amazon AppFlow performs while transferring the data in the flow run.
  name: tasks
  type: array
- description: ''
  name: triggerConfig
  type: object
- description: Specifies when the flow was created.
  name: createdAt
  type: string
- description: Specifies when the flow was last updated.
  name: lastUpdatedAt
  type: string
- description: The tags used to organize, track, or control access for your flow.
  name: tags
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/amazon-appflow-schema.json
slug: amazon-appflow
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: Amazon AppFlow Flow Definition
---
