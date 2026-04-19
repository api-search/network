---
description: ''
layout: schema
name: Method
properties_list:
- description: The method's HTTP verb.
  name: httpMethod
  type: string
- description: The method's authorization type. Valid values are NONE, AWS_IAM, CUSTOM, or COGNITO_USER_POOLS.
  name: authorizationType
  type: string
- description: The identifier of an Authorizer to use on this method.
  name: authorizerId
  type: string
- description: Whether the method requires an API key.
  name: apiKeyRequired
  type: boolean
- description: The identifier of a RequestValidator.
  name: requestValidatorId
  type: string
- description: A human-friendly operation identifier for the method.
  name: operationName
  type: string
- description: Request parameters that can be accepted by the method. Keys identify the parameter location and name.
  name: requestParameters
  type: object
- description: Specifies the Model resources used for the request's content type.
  name: requestModels
  type: object
- description: Method responses keyed by status code.
  name: methodResponses
  type: object
- description: ''
  name: methodIntegration
  type: object
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-method-schema.json
slug: amazon-api-gateway-method
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: Method
---
