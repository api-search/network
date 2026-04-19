---
description: ''
layout: schema
name: BatchGetItemOutput
properties_list:
- description: A map of table name to a list of items
  name: Responses
  type: object
- description: A map of tables and their respective keys that were not processed. Retry these using exponential backoff.
  name: UnprocessedKeys
  type: object
- description: ''
  name: ConsumedCapacity
  type: array
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-batch-get-item-output-schema.json
slug: dynamodb-batch-get-item-output
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: BatchGetItemOutput
---
