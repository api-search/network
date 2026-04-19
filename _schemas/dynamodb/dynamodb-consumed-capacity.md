---
description: ''
layout: schema
name: ConsumedCapacity
properties_list:
- description: The name of the table that was affected by the operation
  name: TableName
  type: string
- description: The total number of capacity units consumed by the operation
  name: CapacityUnits
  type: number
- description: The total number of read capacity units consumed
  name: ReadCapacityUnits
  type: number
- description: The total number of write capacity units consumed
  name: WriteCapacityUnits
  type: number
- description: ''
  name: Table
  type: object
- description: ''
  name: LocalSecondaryIndexes
  type: object
- description: ''
  name: GlobalSecondaryIndexes
  type: object
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-consumed-capacity-schema.json
slug: dynamodb-consumed-capacity
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ConsumedCapacity
---
