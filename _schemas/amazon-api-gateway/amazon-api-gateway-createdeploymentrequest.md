---
description: ''
layout: schema
name: CreateDeploymentRequest
properties_list:
- description: The name of the stage that the deployment is made to. If not specified, a new stage is created with a generated name.
  name: stageName
  type: string
- description: ''
  name: stageDescription
  type: string
- description: A description for the deployment.
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
  name: canarySettings
  type: object
- description: ''
  name: tracingEnabled
  type: boolean
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-createdeploymentrequest-schema.json
slug: amazon-api-gateway-createdeploymentrequest
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: CreateDeploymentRequest
---
