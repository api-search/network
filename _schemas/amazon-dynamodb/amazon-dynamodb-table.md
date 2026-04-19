---
description: Represents an Amazon DynamoDB table with its associated configuration, key schema, throughput settings, indexes, and metadata.
layout: schema
name: Amazon DynamoDB Table
properties_list:
- description: The name of the table
  name: tableName
  type: string
- description: The Amazon Resource Name (ARN) that uniquely identifies the table
  name: tableArn
  type: string
- description: Unique identifier for the table
  name: tableId
  type: string
- description: The current state of the table
  name: tableStatus
  type: string
- description: The date and time when the table was created
  name: creationDateTime
  type: string
- description: The primary key structure for the table, consisting of one or two key elements
  name: keySchema
  type: array
- description: An array of attributes that describe the key schema for the table and indexes
  name: attributeDefinitions
  type: array
- description: ''
  name: provisionedThroughput
  type: object
- description: Controls how you are charged for read and write throughput
  name: billingMode
  type: string
- description: The number of items in the table (updated approximately every six hours)
  name: itemCount
  type: integer
- description: The total size of the table in bytes (updated approximately every six hours)
  name: tableSizeBytes
  type: integer
- description: The global secondary indexes, if any, on the table
  name: globalSecondaryIndexes
  type: array
- description: The local secondary indexes, if any, on the table
  name: localSecondaryIndexes
  type: array
- description: ''
  name: streamSpecification
  type: object
- description: ''
  name: sseDescription
  type: object
- description: Tags assigned to the table
  name: tags
  type: array
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/amazon-dynamodb-table-schema.json
slug: amazon-dynamodb-table
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: Amazon DynamoDB Table
---
