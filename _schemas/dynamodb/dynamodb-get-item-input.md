---
description: ''
layout: schema
name: GetItemInput
properties_list:
- description: The name of the table containing the requested item
  name: TableName
  type: string
- description: A map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve
  name: Key
  type: object
- description: A string that identifies one or more attributes to retrieve from the table
  name: ProjectionExpression
  type: string
- description: One or more substitution tokens for attribute names in an expression
  name: ExpressionAttributeNames
  type: object
- description: If set to true, the operation uses strongly consistent reads; otherwise, eventually consistent reads are used
  name: ConsistentRead
  type: boolean
- description: ''
  name: ReturnConsumedCapacity
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-get-item-input-schema.json
slug: dynamodb-get-item-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: GetItemInput
---
