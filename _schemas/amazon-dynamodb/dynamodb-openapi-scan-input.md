---
description: ScanInput schema from Amazon DynamoDB API
layout: schema
name: ScanInput
properties_list:
- description: The name of the table to scan
  name: TableName
  type: string
- description: The name of a secondary index to scan
  name: IndexName
  type: string
- description: A string that contains conditions for filtering the scan results
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
- description: The maximum number of items to evaluate
  name: Limit
  type: integer
- description: Determines the read consistency model
  name: ConsistentRead
  type: boolean
- description: The primary key of the first item that this operation evaluates
  name: ExclusiveStartKey
  type: object
- description: For parallel scan, identifies the segment to be scanned
  name: Segment
  type: integer
- description: For parallel scan, the total number of segments
  name: TotalSegments
  type: integer
- description: The attributes to be returned in the result
  name: Select
  type: string
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-scan-input-schema.json
slug: dynamodb-openapi-scan-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: ScanInput
---
