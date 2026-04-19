---
description: TransactWriteItemsInput schema from Amazon DynamoDB API
layout: schema
name: TransactWriteItemsInput
properties_list:
- description: An ordered array of up to 100 TransactWriteItem objects
  name: TransactItems
  type: array
- description: A unique identifier for the client request to ensure idempotency
  name: ClientRequestToken
  type: string
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-transact-write-items-input-schema.json
slug: dynamodb-openapi-transact-write-items-input
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: TransactWriteItemsInput
---
