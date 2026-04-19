---
description: Represents the data for an attribute. Each attribute value is described as a name-value pair with the data type as the name.
layout: schema
name: AttributeValue
properties_list:
- description: String attribute value
  name: S
  type: string
- description: Number attribute value (sent as string)
  name: N
  type: string
- description: Binary attribute value (Base64-encoded)
  name: B
  type: string
- description: String set attribute value
  name: SS
  type: array
- description: Number set attribute value
  name: NS
  type: array
- description: Binary set attribute value
  name: BS
  type: array
- description: Map attribute value
  name: M
  type: object
- description: List attribute value
  name: L
  type: array
- description: Null attribute value
  name: 'NULL'
  type: boolean
- description: Boolean attribute value
  name: BOOL
  type: boolean
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-attribute-value-schema.json
slug: dynamodb-openapi-attribute-value
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: AttributeValue
---
