---
description: UpdateTableInput schema from Amazon DynamoDB API
layout: schema
name: UpdateTableInput
properties_list:
- description: The name of the table to update
  name: TableName
  type: string
- description: ''
  name: ProvisionedThroughput
  type: object
- description: ''
  name: BillingMode
  type: string
- description: An array of global secondary index operations
  name: GlobalSecondaryIndexUpdates
  type: array
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-update-table-input-schema.json
slug: dynamodb-openapi-update-table-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: UpdateTableInput
---
