---
description: ''
layout: schema
name: UpdateItemInput
properties_list:
- description: The name of the table containing the item to update
  name: TableName
  type: string
- description: The primary key of the item to update
  name: Key
  type: object
- description: An expression that defines one or more attributes to be updated, the action to be performed on them, and new values for them
  name: UpdateExpression
  type: string
- description: A condition that must be satisfied for the update to succeed
  name: ConditionExpression
  type: string
- description: ''
  name: ExpressionAttributeNames
  type: object
- description: ''
  name: ExpressionAttributeValues
  type: object
- description: Whether to return the item attributes as they appeared before or after the update
  name: ReturnValues
  type: string
- description: ''
  name: ReturnConsumedCapacity
  type: string
- description: ''
  name: ReturnItemCollectionMetrics
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-update-item-input-schema.json
slug: dynamodb-update-item-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: UpdateItemInput
---
