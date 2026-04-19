---
description: ''
layout: schema
name: CreateRestApiRequest
properties_list:
- description: The name of the REST API.
  name: name
  type: string
- description: The description of the REST API.
  name: description
  type: string
- description: A version identifier for the API.
  name: version
  type: string
- description: The ID of the REST API to clone from.
  name: cloneFrom
  type: string
- description: The list of binary media types to support.
  name: binaryMediaTypes
  type: array
- description: Minimum payload compression size in bytes.
  name: minimumCompressionSize
  type: integer
- description: ''
  name: apiKeySource
  type: string
- description: ''
  name: endpointConfiguration
  type: object
- description: ''
  name: policy
  type: string
- description: ''
  name: tags
  type: object
- description: ''
  name: disableExecuteApiEndpoint
  type: boolean
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-createrestapirequest-schema.json
slug: amazon-api-gateway-createrestapirequest
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: CreateRestApiRequest
---
