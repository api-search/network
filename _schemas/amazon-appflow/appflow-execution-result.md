---
description: ExecutionResult schema from Amazon AppFlow API
layout: schema
name: ExecutionResult
properties_list:
- description: Provides any error message information related to the flow run.
  name: errorInfo
  type: object
- description: The total number of bytes processed by the flow run.
  name: bytesProcessed
  type: integer
- description: The total number of bytes written as a result of the flow run.
  name: bytesWritten
  type: integer
- description: The number of records processed in the flow run.
  name: recordsProcessed
  type: integer
- description: The number of processes that Amazon AppFlow ran at the same time when it retrieved your data.
  name: numParallelProcesses
  type: integer
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-execution-result-schema.json
slug: appflow-execution-result
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: ExecutionResult
---
