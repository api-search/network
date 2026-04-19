---
description: UpdateItemInput schema from Amazon DynamoDB API
layout: schema
name: UpdateItemInput
properties_list:
- description: The name of the table containing the item to update
  name: TableName
  type: string
- description: The primary key of the item to be updated
  name: Key
  type: object
- description: An expression that defines attributes to be updated
  name: UpdateExpression
  type: string
- description: A condition that must be satisfied for the update to succeed
  name: ConditionExpression
  type: string
- description: Substitution tokens for attribute names in an expression
  name: ExpressionAttributeNames
  type: object
- description: Values that can be substituted in an expression
  name: ExpressionAttributeValues
  type: object
- description: Determines the return values after the operation
  name: ReturnValues
  type: string
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-update-item-input-schema.json
slug: dynamodb-openapi-update-item-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: UpdateItemInput
---
