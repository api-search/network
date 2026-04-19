---
description: ''
layout: schema
name: ScanOutput
properties_list:
- description: An array of item attributes that match the scan criteria
  name: Items
  type: array
- description: The number of items in the response
  name: Count
  type: integer
- description: The number of items evaluated before any filter was applied
  name: ScannedCount
  type: integer
- description: The primary key of the item where the operation stopped. Use this value for ExclusiveStartKey in a new request to continue the scan.
  name: LastEvaluatedKey
  type: object
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-scan-output-schema.json
slug: dynamodb-scan-output
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ScanOutput
---
