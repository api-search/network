---
description: ''
layout: schema
name: MethodSetting
properties_list:
- description: ''
  name: metricsEnabled
  type: boolean
- description: ''
  name: loggingLevel
  type: string
- description: ''
  name: dataTraceEnabled
  type: boolean
- description: ''
  name: throttlingBurstLimit
  type: integer
- description: ''
  name: throttlingRateLimit
  type: number
- description: ''
  name: cachingEnabled
  type: boolean
- description: ''
  name: cacheTtlInSeconds
  type: integer
- description: ''
  name: cacheDataEncrypted
  type: boolean
- description: ''
  name: requireAuthorizationForCacheControl
  type: boolean
- description: ''
  name: unauthorizedCacheControlHeaderStrategy
  type: string
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-methodsetting-schema.json
slug: amazon-api-gateway-methodsetting
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: MethodSetting
---
