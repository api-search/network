---
description: ''
layout: schema
name: SSESpecification
properties_list:
- description: Indicates whether server-side encryption is enabled
  name: Enabled
  type: boolean
- description: Server-side encryption type
  name: SSEType
  type: string
- description: The KMS key that should be used for server-side encryption
  name: KMSMasterKeyId
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-sse-specification-schema.json
slug: dynamodb-sse-specification
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: SSESpecification
---
