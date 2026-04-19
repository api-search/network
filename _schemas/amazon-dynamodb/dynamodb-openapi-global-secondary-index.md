---
description: Represents the properties of a global secondary index
layout: schema
name: GlobalSecondaryIndex
properties_list:
- description: The name of the global secondary index
  name: IndexName
  type: string
- description: The complete key schema for the index
  name: KeySchema
  type: array
- description: ''
  name: Projection
  type: object
- description: ''
  name: ProvisionedThroughput
  type: object
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-global-secondary-index-schema.json
slug: dynamodb-openapi-global-secondary-index
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: GlobalSecondaryIndex
---
