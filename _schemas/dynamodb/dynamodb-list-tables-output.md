---
description: ''
layout: schema
name: ListTablesOutput
properties_list:
- description: The names of the tables associated with the current account
  name: TableNames
  type: array
- description: The name of the last table in the current page of results. Use this value as ExclusiveStartTableName for the next request.
  name: LastEvaluatedTableName
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-list-tables-output-schema.json
slug: dynamodb-list-tables-output
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ListTablesOutput
---
