---
description: Specification for a RateLimit resource
layout: schema
name: RateLimitSpec
properties_list:
- description: Rate limiting domain that groups related rate limit configurations. Typically set to 'ambassador'.
  name: domain
  type: string
- description: List of rate limit rules
  name: limits
  type: array
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-rate-limit-spec-schema.json
slug: ambassador-rate-limit-spec
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: RateLimitSpec
---
