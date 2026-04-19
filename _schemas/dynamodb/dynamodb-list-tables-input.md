---
description: ''
layout: schema
name: ListTablesInput
properties_list:
- description: The first table name that this operation will evaluate. Use the value returned for LastEvaluatedTableName in a previous operation.
  name: ExclusiveStartTableName
  type: string
- description: Maximum number of table names to return (1-100)
  name: Limit
  type: integer
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-list-tables-input-schema.json
slug: dynamodb-list-tables-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ListTablesInput
---
