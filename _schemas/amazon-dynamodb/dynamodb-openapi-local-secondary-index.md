---
description: Represents the properties of a local secondary index
layout: schema
name: LocalSecondaryIndex
properties_list:
- description: The name of the local secondary index
  name: IndexName
  type: string
- description: The complete key schema for the index
  name: KeySchema
  type: array
- description: ''
  name: Projection
  type: object
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-local-secondary-index-schema.json
slug: dynamodb-openapi-local-secondary-index
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: LocalSecondaryIndex
---
