---
description: ''
layout: schema
name: DeleteItemInput
properties_list:
- description: The name of the table from which to delete the item
  name: TableName
  type: string
- description: The primary key of the item to delete
  name: Key
  type: object
- description: A condition that must be satisfied for the deletion to succeed
  name: ConditionExpression
  type: string
- description: ''
  name: ExpressionAttributeNames
  type: object
- description: ''
  name: ExpressionAttributeValues
  type: object
- description: Whether to return the item attributes as they appeared before deletion
  name: ReturnValues
  type: string
- description: ''
  name: ReturnConsumedCapacity
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-delete-item-input-schema.json
slug: dynamodb-delete-item-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: DeleteItemInput
---
