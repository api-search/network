---
description: ''
layout: schema
name: Stage
properties_list:
- description: The identifier of the deployment attached to this stage.
  name: deploymentId
  type: string
- description: The identifier of a client certificate for an API stage.
  name: clientCertificateId
  type: string
- description: The name of the stage.
  name: stageName
  type: string
- description: The stage's description.
  name: description
  type: string
- description: Whether cache clustering is enabled for the stage.
  name: cacheClusterEnabled
  type: boolean
- description: The stage's cache cluster size.
  name: cacheClusterSize
  type: string
- description: ''
  name: cacheClusterStatus
  type: string
- description: ''
  name: methodSettings
  type: object
- description: Stage variables.
  name: variables
  type: object
- description: ''
  name: documentationVersion
  type: string
- description: ''
  name: accessLogSettings
  type: object
- description: ''
  name: canarySettings
  type: object
- description: Whether X-Ray tracing is enabled for this stage.
  name: tracingEnabled
  type: boolean
- description: The ARN of the WebAcl associated with the stage.
  name: webAclArn
  type: string
- description: ''
  name: tags
  type: object
- description: ''
  name: createdDate
  type: string
- description: ''
  name: lastUpdatedDate
  type: string
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-stage-schema.json
slug: amazon-api-gateway-stage
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: Stage
---
