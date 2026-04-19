---
description: DescribeFlowResponse schema from Amazon AppFlow API
layout: schema
name: DescribeFlowResponse
properties_list:
- description: The flow's Amazon Resource Name (ARN).
  name: flowArn
  type: string
- description: A description of the flow.
  name: description
  type: string
- description: The specified name of the flow.
  name: flowName
  type: string
- description: The ARN of the AWS KMS key.
  name: kmsArn
  type: string
- description: Indicates the current status of the flow.
  name: flowStatus
  type: string
- description: Contains an error message if the flow status is in a suspended or error state.
  name: flowStatusMessage
  type: string
- description: ''
  name: sourceFlowConfig
  type: object
- description: ''
  name: destinationFlowConfigList
  type: array
- description: ''
  name: lastRunExecutionDetails
  type: object
- description: ''
  name: triggerConfig
  type: object
- description: ''
  name: tasks
  type: array
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
  name: metadataCatalogConfig
  type: object
- description: ''
  name: lastRunMetadataCatalogDetails
  type: array
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-describe-flow-response-schema.json
slug: appflow-describe-flow-response
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: DescribeFlowResponse
---
