---
description: CreateTableInput schema from Amazon DynamoDB API
layout: schema
name: CreateTableInput
properties_list:
- description: The name of the table to create
  name: TableName
  type: string
- description: Specifies the attributes that make up the primary key for the table. The attributes must also be defined in AttributeDefinitions.
  name: KeySchema
  type: array
- description: An array of attributes that describe the key schema for the table and indexes
  name: AttributeDefinitions
  type: array
- description: ''
  name: ProvisionedThroughput
  type: object
- description: Controls how you are charged for read and write throughput
  name: BillingMode
  type: string
- description: One or more global secondary indexes to be created on the table
  name: GlobalSecondaryIndexes
  type: array
- description: One or more local secondary indexes to be created on the table
  name: LocalSecondaryIndexes
  type: array
- description: Tags to associate with the table
  name: Tags
  type: array
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-create-table-input-schema.json
slug: dynamodb-openapi-create-table-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: CreateTableInput
---
