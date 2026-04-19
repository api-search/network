---
description: ''
layout: schema
name: ImportTableInput
properties_list:
- description: Idempotency token
  name: ClientToken
  type: string
- description: ''
  name: S3BucketSource
  type: object
- description: ''
  name: InputFormat
  type: string
- description: ''
  name: InputFormatOptions
  type: object
- description: ''
  name: InputCompressionType
  type: string
- description: ''
  name: TableCreationParameters
  type: object
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-import-table-input-schema.json
slug: dynamodb-import-table-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ImportTableInput
---
