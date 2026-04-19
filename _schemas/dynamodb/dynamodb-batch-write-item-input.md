---
description: ''
layout: schema
name: BatchWriteItemInput
properties_list:
- description: A map of one or more table names and, for each table, a list of operations to perform (PutRequest or DeleteRequest)
  name: RequestItems
  type: object
- description: ''
  name: ReturnConsumedCapacity
  type: string
- description: ''
  name: ReturnItemCollectionMetrics
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-batch-write-item-input-schema.json
slug: dynamodb-batch-write-item-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: BatchWriteItemInput
---
