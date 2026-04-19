---
description: ''
layout: schema
name: QueryOutput
properties_list:
- description: An array of item attributes that match the query criteria
  name: Items
  type: array
- description: The number of items in the response
  name: Count
  type: integer
- description: The number of items evaluated before any filter was applied
  name: ScannedCount
  type: integer
- description: The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value for ExclusiveStartKey in a new request to continue the query.
  name: LastEvaluatedKey
  type: object
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-query-output-schema.json
slug: dynamodb-query-output
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: QueryOutput
---
