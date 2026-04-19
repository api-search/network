---
description: ''
layout: schema
name: Authorizer
properties_list:
- description: The identifier of the authorizer.
  name: id
  type: string
- description: The name of the authorizer.
  name: name
  type: string
- description: The authorizer type.
  name: type
  type: string
- description: A list of the Amazon Cognito user pool ARNs.
  name: providerARNs
  type: array
- description: An optional customer-defined field for authorization type.
  name: authType
  type: string
- description: The authorizer's URI. For TOKEN or REQUEST authorizers, this is the Lambda function URI.
  name: authorizerUri
  type: string
- description: The credentials required for the authorizer as an IAM role ARN.
  name: authorizerCredentials
  type: string
- description: The identity source for which authorization is requested.
  name: identitySource
  type: string
- description: A validation expression for the incoming identity token.
  name: identityValidationExpression
  type: string
- description: The TTL in seconds of cached authorizer results. Max 3600.
  name: authorizerResultTtlInSeconds
  type: integer
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-authorizer-schema.json
slug: amazon-api-gateway-authorizer
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: Authorizer
---
