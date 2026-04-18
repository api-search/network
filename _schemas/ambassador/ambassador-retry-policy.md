---
description: Retry configuration for failed requests
layout: schema
name: RetryPolicy
properties_list:
- description: Envoy retry condition. Common values include 5xx, gateway-error, connect-failure, retriable-4xx.
  name: retry_on
  type: string
- description: Maximum number of retry attempts
  name: num_retries
  type: integer
- description: Timeout per retry attempt (e.g., '3s', '500ms')
  name: per_try_timeout
  type: string
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-retry-policy-schema.json
slug: ambassador-retry-policy
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: RetryPolicy
---
