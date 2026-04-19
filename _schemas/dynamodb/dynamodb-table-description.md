---
description: ''
layout: schema
name: TableDescription
properties_list:
- description: The name of the table
  name: TableName
  type: string
- description: The current state of the table
  name: TableStatus
  type: string
- description: The Amazon Resource Name (ARN) of the table
  name: TableArn
  type: string
- description: Unique identifier for the table
  name: TableId
  type: string
- description: The total size of the specified table in bytes
  name: TableSizeBytes
  type: integer
- description: The number of items in the specified table
  name: ItemCount
  type: integer
- description: The date and time when the table was created
  name: CreationDateTime
  type: string
- description: An array of AttributeDefinition objects
  name: AttributeDefinitions
  type: array
- description: The primary key structure for the table
  name: KeySchema
  type: array
- description: ''
  name: BillingModeSummary
  type: object
- description: ''
  name: GlobalSecondaryIndexes
  type: array
- description: ''
  name: LocalSecondaryIndexes
  type: array
- description: A timestamp in ISO 8601 format of the stream label
  name: LatestStreamLabel
  type: string
- description: The ARN of the latest DynamoDB stream
  name: LatestStreamArn
  type: string
- description: Indicates whether deletion protection is enabled
  name: DeletionProtectionEnabled
  type: boolean
- description: ''
  name: TableClassSummary
  type: object
- description: ''
  name: SSEDescription
  type: object
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-table-description-schema.json
slug: dynamodb-table-description
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: TableDescription
---
