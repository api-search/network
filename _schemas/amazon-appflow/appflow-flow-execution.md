---
description: FlowExecution schema from Amazon AppFlow API
layout: schema
name: FlowExecution
properties_list:
- description: Specifies the identifier of the given flow run.
  name: executionId
  type: string
- description: Specifies the flow run status and whether it is in progress, has completed successfully, or has failed.
  name: executionStatus
  type: string
- description: ''
  name: executionResult
  type: object
- description: Specifies the start timestamp for your flow run.
  name: startedAt
  type: integer
- description: Specifies the time of the most recent update.
  name: lastUpdatedAt
  type: integer
- description: The timestamp that determines the first new or updated record to be transferred in the flow run.
  name: dataPullStartTime
  type: integer
- description: The timestamp that determines the last new or updated record to be transferred in the flow run.
  name: dataPullEndTime
  type: integer
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-flow-execution-schema.json
slug: appflow-flow-execution
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: FlowExecution
---
