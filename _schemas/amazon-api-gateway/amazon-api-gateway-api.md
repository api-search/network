---
description: Schema defining the structure of an Amazon API Gateway REST API resource, including its configuration for resources, methods, integrations, stages, deployments, authorizers, models, and associated settings.
layout: schema
name: Amazon API Gateway REST API Definition
properties_list:
- description: The unique identifier of the REST API assigned by API Gateway.
  name: id
  type: string
- description: The name of the REST API.
  name: name
  type: string
- description: A human-readable description of the REST API.
  name: description
  type: string
- description: A version identifier for the API.
  name: version
  type: string
- description: The timestamp when the REST API was created.
  name: createdDate
  type: string
- description: The source of the API key for metering requests according to a usage plan. HEADER reads the key from the X-API-Key header. AUTHORIZER reads it from the UsageIdentifierKey from a custom authorizer.
  name: apiKeySource
  type: string
- description: The list of binary media types supported by the REST API, such as image/png or application/octet-stream.
  name: binaryMediaTypes
  type: array
- description: 'A nullable integer that is used to enable or disable compression on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than '
  name: minimumCompressionSize
  type: integer
- description: ''
  name: endpointConfiguration
  type: object
- description: A stringified JSON policy document that applies to this REST API regardless of the caller and method configuration.
  name: policy
  type: string
- description: The collection of tags associated with the REST API. Each tag is a key-value pair.
  name: tags
  type: object
- description: Specifies whether clients can invoke your API by using the default execute-api endpoint. When true, clients must use a custom domain name to invoke the API.
  name: disableExecuteApiEndpoint
  type: boolean
- description: The collection of API resources defining the URL structure.
  name: resources
  type: array
- description: The named stages of the API deployment lifecycle.
  name: stages
  type: array
- description: Snapshots of the API configuration that are deployed to stages.
  name: deployments
  type: array
- description: Authorization mechanisms configured for the API.
  name: authorizers
  type: array
- description: Data models that define the structure of request and response payloads.
  name: models
  type: array
- description: Request validators that check incoming requests before passing them to integrations.
  name: requestValidators
  type: array
- description: Customized gateway responses for various error types.
  name: gatewayResponses
  type: array
- description: Documentation content associated with API entities.
  name: documentationParts
  type: array
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-api-schema.json
slug: amazon-api-gateway-api
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: Amazon API Gateway REST API Definition
---
