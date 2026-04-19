---
description: ScanOutput schema from Amazon DynamoDB API
layout: schema
name: ScanOutput
properties_list:
- description: An array of item attributes that match the scan criteria
  name: Items
  type: array
- description: The number of items in the response
  name: Count
  type: integer
- description: The number of items evaluated before any filter is applied
  name: ScannedCount
  type: integer
- description: The primary key of the item where the operation stopped
  name: LastEvaluatedKey
  type: object
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-scan-output-schema.json
slug: dynamodb-openapi-scan-output
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: ScanOutput
---
