---
description: ''
layout: schema
name: Integration
properties_list:
- description: The integration input's type.
  name: type
  type: string
- description: The integration's HTTP method type.
  name: httpMethod
  type: string
- description: The Uniform Resource Identifier (URI) for the integration.
  name: uri
  type: string
- description: The type of the network connection to the integration endpoint.
  name: connectionType
  type: string
- description: The ID of the VPC link used for the integration when connectionType is VPC_LINK.
  name: connectionId
  type: string
- description: The credentials required for the integration, if any. For AWS integrations, three options are available.
  name: credentials
  type: string
- description: ''
  name: requestParameters
  type: object
- description: ''
  name: requestTemplates
  type: object
- description: ''
  name: passthroughBehavior
  type: string
- description: ''
  name: contentHandling
  type: string
- description: Custom timeout between 50 and 29000 milliseconds.
  name: timeoutInMillis
  type: integer
- description: ''
  name: cacheNamespace
  type: string
- description: ''
  name: cacheKeyParameters
  type: array
- description: ''
  name: integrationResponses
  type: object
- description: ''
  name: tlsConfig
  type: object
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-integration-schema.json
slug: amazon-api-gateway-integration
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: Integration
---
