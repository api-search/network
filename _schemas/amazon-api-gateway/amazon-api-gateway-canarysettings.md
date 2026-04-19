---
description: ''
layout: schema
name: CanarySettings
properties_list:
- description: The percent of traffic the canary deployment receives.
  name: percentTraffic
  type: number
- description: ''
  name: deploymentId
  type: string
- description: ''
  name: stageVariableOverrides
  type: object
- description: ''
  name: useStageCache
  type: boolean
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-canarysettings-schema.json
slug: amazon-api-gateway-canarysettings
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: CanarySettings
---
