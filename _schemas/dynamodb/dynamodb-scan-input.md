---
description: ''
layout: schema
name: ScanInput
properties_list:
- description: The name of the table containing the requested items
  name: TableName
  type: string
- description: The name of a secondary index to scan
  name: IndexName
  type: string
- description: A string that contains conditions that DynamoDB applies after the Scan operation, but before the data is returned
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
- description: ''
  name: Select
  type: string
- description: The maximum number of items to evaluate
  name: Limit
  type: integer
- description: Whether to use strongly consistent reads
  name: ConsistentRead
  type: boolean
- description: The primary key of the first item for this scan to evaluate
  name: ExclusiveStartKey
  type: object
- description: Identifies an individual segment to be scanned by a parallel scan
  name: Segment
  type: integer
- description: Total number of segments for a parallel scan
  name: TotalSegments
  type: integer
- description: ''
  name: ReturnConsumedCapacity
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-scan-input-schema.json
slug: dynamodb-scan-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ScanInput
---
