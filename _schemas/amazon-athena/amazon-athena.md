---
description: Schema defining the structure of an Amazon Athena query execution resource, including query string, execution context, result configuration, work group settings, and execution status.
layout: schema
name: Amazon Athena Query Execution
properties_list:
- description: The unique identifier for each query execution.
  name: QueryExecutionId
  type: string
- description: The SQL query statements which the query execution ran.
  name: QueryString
  type: string
- description: The type of query statement that was run.
  name: StatementType
  type: string
- description: ''
  name: ResultConfiguration
  type: object
- description: ''
  name: QueryExecutionContext
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: Statistics
  type: object
- description: The name of the workgroup in which the query ran.
  name: WorkGroup
  type: string
- description: ''
  name: EngineVersion
  type: object
- description: A list of values for the parameters in a query.
  name: ExecutionParameters
  type: array
- description: The kind of query statement that was run.
  name: SubstatementType
  type: string
provider_name: Amazon Athena
provider_slug: amazon-athena
schema_file: json-schema/amazon-athena-schema.json
slug: amazon-athena
tags:
- Amazon Athena
- SQL
- Analytics
- Serverless
- AWS
title: Amazon Athena Query Execution
---
