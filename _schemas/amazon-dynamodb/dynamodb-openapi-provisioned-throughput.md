---
description: Represents the provisioned throughput settings for a table or index
layout: schema
name: ProvisionedThroughput
properties_list:
- description: The maximum number of strongly consistent reads per second
  name: ReadCapacityUnits
  type: integer
- description: The maximum number of writes per second
  name: WriteCapacityUnits
  type: integer
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
schema_file: json-schema/dynamodb-openapi-provisioned-throughput-schema.json
slug: dynamodb-openapi-provisioned-throughput
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
title: ProvisionedThroughput
---
