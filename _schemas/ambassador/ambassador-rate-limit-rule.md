---
description: A single rate limiting rule with a pattern and rate
layout: schema
name: RateLimitRule
properties_list:
- description: Descriptor entries to match against. Each entry is a key-value pair that must match the labels sent with the request.
  name: pattern
  type: array
- description: Maximum number of requests allowed in the specified unit of time
  name: rate
  type: integer
- description: Time unit for the rate limit
  name: unit
  type: string
- description: Headers to inject into the request when the rate limit is applied
  name: injectRequestHeaders
  type: array
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-rate-limit-rule-schema.json
slug: ambassador-rate-limit-rule
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: RateLimitRule
---
