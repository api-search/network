---
description: ''
layout: schema
name: TransactWriteItemsInput
properties_list:
- description: An ordered array of up to 100 TransactWriteItem objects
  name: TransactItems
  type: array
- description: Unique identifier for the idempotency of the request
  name: ClientRequestToken
  type: string
- description: ''
  name: ReturnConsumedCapacity
  type: string
- description: ''
  name: ReturnItemCollectionMetrics
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-transact-write-items-input-schema.json
slug: dynamodb-transact-write-items-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: TransactWriteItemsInput
---
