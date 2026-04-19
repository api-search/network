---
description: JSON Schema for Amazon DynamoDB items, attribute values, table definitions, and stream records. DynamoDB uses a JSON-based data format with type descriptors where each attribute value is represented as a name-value pair with the name being the data type indicator (S, N, B, BOOL, NULL, L, M, SS, NS, BS).
layout: schema
name: Amazon DynamoDB Item Schema
properties_list:
- description: A single DynamoDB item
  name: item
  type: object
- description: A primary key for identifying an item
  name: key
  type: object
- description: A complete DynamoDB table definition
  name: tableDefinition
  type: object
- description: A DynamoDB Streams record
  name: streamRecord
  type: object
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-item-schema.json
slug: dynamodb-item
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: Amazon DynamoDB Item Schema
---
