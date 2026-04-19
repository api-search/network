---
description: ''
layout: schema
name: RestApi
properties_list:
- description: The API's identifier.
  name: id
  type: string
- description: The API's name.
  name: name
  type: string
- description: The API's description.
  name: description
  type: string
- description: The timestamp when the API was created.
  name: createdDate
  type: string
- description: A version identifier for the API.
  name: version
  type: string
- description: The warning messages reported when failonwarnings is on.
  name: warnings
  type: array
- description: The list of binary media types supported by the REST API.
  name: binaryMediaTypes
  type: array
- description: A nullable integer for the minimum payload size in bytes to compress.
  name: minimumCompressionSize
  type: integer
- description: The source of the API key for metering requests.
  name: apiKeySource
  type: string
- description: ''
  name: endpointConfiguration
  type: object
- description: A stringified JSON policy document that applies to this REST API.
  name: policy
  type: string
- description: Tags attached to the REST API.
  name: tags
  type: object
- description: Specifies whether clients can invoke your API by using the default execute-api endpoint.
  name: disableExecuteApiEndpoint
  type: boolean
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-restapi-schema.json
slug: amazon-api-gateway-restapi
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: RestApi
---
