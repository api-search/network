---
description: ''
layout: schema
name: CreateStageRequest
properties_list:
- description: The name for the stage.
  name: stageName
  type: string
- description: The identifier of the deployment.
  name: deploymentId
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: cacheClusterEnabled
  type: boolean
- description: ''
  name: cacheClusterSize
  type: string
- description: ''
  name: variables
  type: object
- description: ''
  name: documentationVersion
  type: string
- description: ''
  name: canarySettings
  type: object
- description: ''
  name: tracingEnabled
  type: boolean
- description: ''
  name: tags
  type: object
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-createstagerequest-schema.json
slug: amazon-api-gateway-createstagerequest
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: CreateStageRequest
---
