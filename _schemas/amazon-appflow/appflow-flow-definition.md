---
description: FlowDefinition schema from Amazon AppFlow API
layout: schema
name: FlowDefinition
properties_list:
- description: The flow's Amazon Resource Name (ARN).
  name: flowArn
  type: string
- description: A user-entered description of the flow.
  name: description
  type: string
- description: The specified name of the flow.
  name: flowName
  type: string
- description: Indicates the current status of the flow.
  name: flowStatus
  type: string
- description: Specifies the source connector type.
  name: sourceConnectorType
  type: string
- description: The label of the source connector in the flow.
  name: sourceConnectorLabel
  type: string
- description: Specifies the destination connector type.
  name: destinationConnectorType
  type: string
- description: The label of the destination connector in the flow.
  name: destinationConnectorLabel
  type: string
- description: Specifies the type of flow trigger.
  name: triggerType
  type: string
- description: Specifies when the flow was created.
  name: createdAt
  type: integer
- description: Specifies when the flow was last updated.
  name: lastUpdatedAt
  type: integer
- description: The ARN of the user who created the flow.
  name: createdBy
  type: string
- description: Specifies the account user name that most recently updated the flow.
  name: lastUpdatedBy
  type: string
- description: ''
  name: tags
  type: object
- description: ''
  name: lastRunExecutionDetails
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-flow-definition-schema.json
slug: appflow-flow-definition
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: FlowDefinition
---
