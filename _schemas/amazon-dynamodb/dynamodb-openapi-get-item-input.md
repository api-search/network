---
description: GetItemInput schema from Amazon DynamoDB API
layout: schema
name: GetItemInput
properties_list:
- description: The name of the table containing the requested item
  name: TableName
  type: string
- description: A map of attribute names to AttributeValue objects for the primary key
  name: Key
  type: object
- description: A string that identifies attributes to retrieve
  name: ProjectionExpression
  type: string
- description: Determines the read consistency model
  name: ConsistentRead
  type: boolean
- description: Substitution tokens for attribute names in an expression
  name: ExpressionAttributeNames
  type: object
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-get-item-input-schema.json
slug: dynamodb-openapi-get-item-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: GetItemInput
---
