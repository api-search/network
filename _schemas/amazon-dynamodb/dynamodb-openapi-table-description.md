---
description: Represents the properties of a DynamoDB table
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
- description: The date and time when the table was created
  name: CreationDateTime
  type: number
- description: The primary key structure for the table
  name: KeySchema
  type: array
- description: An array of attribute definitions for the table
  name: AttributeDefinitions
  type: array
- description: ''
  name: ProvisionedThroughput
  type: object
- description: The total size of the table in bytes
  name: TableSizeBytes
  type: integer
- description: The number of items in the table
  name: ItemCount
  type: integer
- description: The global secondary indexes on the table
  name: GlobalSecondaryIndexes
  type: array
- description: The local secondary indexes on the table
  name: LocalSecondaryIndexes
  type: array
- description: Contains details about the billing mode for the table
  name: BillingModeSummary
  type: object
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-table-description-schema.json
slug: dynamodb-openapi-table-description
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: TableDescription
---
