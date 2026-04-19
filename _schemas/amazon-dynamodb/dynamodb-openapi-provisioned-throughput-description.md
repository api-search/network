---
description: Describes the provisioned throughput settings for a table or index
layout: schema
name: ProvisionedThroughputDescription
properties_list:
- description: The date and time of the last provisioned throughput increase
  name: LastIncreaseDateTime
  type: number
- description: The date and time of the last provisioned throughput decrease
  name: LastDecreaseDateTime
  type: number
- description: The number of provisioned throughput decreases for this table during this UTC calendar day
  name: NumberOfDecreasesToday
  type: integer
- description: The maximum number of strongly consistent reads per second
  name: ReadCapacityUnits
  type: integer
- description: The maximum number of writes per second
  name: WriteCapacityUnits
  type: integer
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-provisioned-throughput-description-schema.json
slug: dynamodb-openapi-provisioned-throughput-description
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: ProvisionedThroughputDescription
---
