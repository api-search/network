---
description: ''
layout: schema
name: ApiKey
properties_list:
- description: The identifier of the API key.
  name: id
  type: string
- description: The value of the API key.
  name: value
  type: string
- description: The name of the API key.
  name: name
  type: string
- description: An AWS Marketplace customer identifier.
  name: customerId
  type: string
- description: ''
  name: description
  type: string
- description: Whether the API key can be used by callers.
  name: enabled
  type: boolean
- description: ''
  name: createdDate
  type: string
- description: ''
  name: lastUpdatedDate
  type: string
- description: ''
  name: stageKeys
  type: array
- description: ''
  name: tags
  type: object
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-apikey-schema.json
slug: amazon-api-gateway-apikey
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: ApiKey
---
