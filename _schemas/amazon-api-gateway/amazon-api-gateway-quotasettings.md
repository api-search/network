---
description: ''
layout: schema
name: QuotaSettings
properties_list:
- description: The maximum number of requests per time period.
  name: limit
  type: integer
- description: The day that a time period starts.
  name: offset
  type: integer
- description: The time period for which the maximum limit applies.
  name: period
  type: string
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-quotasettings-schema.json
slug: amazon-api-gateway-quotasettings
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: QuotaSettings
---
