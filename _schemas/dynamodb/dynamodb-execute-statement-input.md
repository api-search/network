---
description: ''
layout: schema
name: ExecuteStatementInput
properties_list:
- description: The PartiQL statement representing the operation to run
  name: Statement
  type: string
- description: The parameters for the PartiQL statement
  name: Parameters
  type: array
- description: The consistency of a read operation
  name: ConsistentRead
  type: boolean
- description: Set this value to get remaining results
  name: NextToken
  type: string
- description: ''
  name: ReturnConsumedCapacity
  type: string
- description: The maximum number of items to evaluate
  name: Limit
  type: integer
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-execute-statement-input-schema.json
slug: dynamodb-execute-statement-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ExecuteStatementInput
---
