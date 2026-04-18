---
description: ''
layout: schema
name: GatewayInput
properties_list:
- description: The name of the gateway.
  name: name
  type: string
- description: Enable response caching.
  name: cache_enabled
  type: boolean
- description: Cache TTL in seconds.
  name: cache_ttl
  type: integer
- description: Enable rate limiting.
  name: rate_limiting_enabled
  type: boolean
- description: Rate limit threshold.
  name: rate_limiting_limit
  type: integer
- description: Rate limiting interval in seconds.
  name: rate_limiting_interval
  type: integer
- description: Enable request logging.
  name: log_enabled
  type: boolean
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-ai-gateway-gateway-input-schema.json
slug: cloudflare-ai-gateway-gateway-input
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
title: GatewayInput
---
