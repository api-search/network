---
description: PutItemInput schema from Amazon DynamoDB API
layout: schema
name: PutItemInput
properties_list:
- description: The name of the table to contain the item
  name: TableName
  type: string
- description: A map of attribute name to attribute values, representing the item
  name: Item
  type: object
- description: A condition that must be satisfied for a put to succeed
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
schema_file: json-schema/dynamodb-openapi-put-item-input-schema.json
slug: dynamodb-openapi-put-item-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: PutItemInput
---
