---
description: Represents attributes that are copied from the table into an index
layout: schema
name: Projection
properties_list:
- description: The set of attributes that are projected into the index
  name: ProjectionType
  type: string
- description: The non-key projected attributes
  name: NonKeyAttributes
  type: array
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-projection-schema.json
slug: dynamodb-openapi-projection
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: Projection
---
