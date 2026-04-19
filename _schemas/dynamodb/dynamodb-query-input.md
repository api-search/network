---
description: ''
layout: schema
name: QueryInput
properties_list:
- description: The name of the table containing the requested items
  name: TableName
  type: string
- description: The name of a secondary index to query
  name: IndexName
  type: string
- description: The condition that specifies the key values for items to be retrieved by the Query action. Must specify the partition key name and value as an equality condition.
  name: KeyConditionExpression
  type: string
- description: A string that contains conditions that DynamoDB applies after the Query operation, but before the data is returned
  name: FilterExpression
  type: string
- description: A string that identifies attributes to retrieve from the table
  name: ProjectionExpression
  type: string
- description: ''
  name: ExpressionAttributeNames
  type: object
- description: ''
  name: ExpressionAttributeValues
  type: object
- description: The attributes to be returned in the result
  name: Select
  type: string
- description: If true (default), the traversal is performed in ascending order; if false, in descending order
  name: ScanIndexForward
  type: boolean
- description: The maximum number of items to evaluate
  name: Limit
  type: integer
- description: Whether to use strongly consistent reads
  name: ConsistentRead
  type: boolean
- description: The primary key of the first item for this query to evaluate
  name: ExclusiveStartKey
  type: object
- description: ''
  name: ReturnConsumedCapacity
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-query-input-schema.json
slug: dynamodb-query-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: QueryInput
---
