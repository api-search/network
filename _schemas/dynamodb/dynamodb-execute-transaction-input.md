---
description: ''
layout: schema
name: ExecuteTransactionInput
properties_list:
- description: The list of PartiQL statements representing the transaction to run
  name: TransactStatements
  type: array
- description: Unique identifier for idempotency
  name: ClientRequestToken
  type: string
- description: ''
  name: ReturnConsumedCapacity
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-execute-transaction-input-schema.json
slug: dynamodb-execute-transaction-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ExecuteTransactionInput
---
