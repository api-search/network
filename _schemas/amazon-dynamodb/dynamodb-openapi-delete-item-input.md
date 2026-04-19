---
description: DeleteItemInput schema from Amazon DynamoDB API
layout: schema
name: DeleteItemInput
properties_list:
- description: The name of the table from which to delete the item
  name: TableName
  type: string
- description: A map of attribute names to AttributeValue objects for the primary key
  name: Key
  type: object
- description: A condition that must be satisfied for the delete to succeed
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
schema_file: json-schema/dynamodb-openapi-delete-item-input-schema.json
slug: dynamodb-openapi-delete-item-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: DeleteItemInput
---
