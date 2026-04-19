---
description: ''
layout: schema
name: PutMethodRequest
properties_list:
- description: The method's authorization type. Valid values are NONE, AWS_IAM, CUSTOM, or COGNITO_USER_POOLS.
  name: authorizationType
  type: string
- description: ''
  name: authorizerId
  type: string
- description: ''
  name: apiKeyRequired
  type: boolean
- description: ''
  name: operationName
  type: string
- description: ''
  name: requestParameters
  type: object
- description: ''
  name: requestModels
  type: object
- description: ''
  name: requestValidatorId
  type: string
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-putmethodrequest-schema.json
slug: amazon-api-gateway-putmethodrequest
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: PutMethodRequest
---
