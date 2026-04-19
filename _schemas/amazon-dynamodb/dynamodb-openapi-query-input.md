---
description: QueryInput schema from Amazon DynamoDB API
layout: schema
name: QueryInput
properties_list:
- description: The name of the table to query
  name: TableName
  type: string
- description: The name of a secondary index to query
  name: IndexName
  type: string
- description: The condition that specifies the key values for items to be retrieved
  name: KeyConditionExpression
  type: string
- description: A string that contains conditions for filtering the query results
  name: FilterExpression
  type: string
- description: A string that identifies attributes to retrieve
  name: ProjectionExpression
  type: string
- description: Substitution tokens for attribute names in an expression
  name: ExpressionAttributeNames
  type: object
- description: Values that can be substituted in an expression
  name: ExpressionAttributeValues
  type: object
- description: Specifies the order for index traversal (true=ascending, false=descending)
  name: ScanIndexForward
  type: boolean
- description: The maximum number of items to evaluate
  name: Limit
  type: integer
- description: Determines the read consistency model
  name: ConsistentRead
  type: boolean
- description: The primary key of the first item that this operation evaluates
  name: ExclusiveStartKey
  type: object
- description: The attributes to be returned in the result
  name: Select
  type: string
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-query-input-schema.json
slug: dynamodb-openapi-query-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: QueryInput
---
