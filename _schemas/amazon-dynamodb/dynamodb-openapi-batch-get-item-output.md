---
description: BatchGetItemOutput schema from Amazon DynamoDB API
layout: schema
name: BatchGetItemOutput
properties_list:
- description: A map of table names to lists of items retrieved
  name: Responses
  type: object
- description: A map of unprocessed keys, to be retried
  name: UnprocessedKeys
  type: object
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-batch-get-item-output-schema.json
slug: dynamodb-openapi-batch-get-item-output
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: BatchGetItemOutput
---
