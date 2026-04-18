---
description: Circuit breaker configuration for an upstream cluster
layout: schema
name: CircuitBreaker
properties_list:
- description: Envoy routing priority
  name: priority
  type: string
- description: Maximum number of connections to the upstream cluster
  name: max_connections
  type: integer
- description: Maximum number of pending requests to the upstream cluster
  name: max_pending_requests
  type: integer
- description: Maximum number of parallel requests to the upstream cluster
  name: max_requests
  type: integer
- description: Maximum number of parallel retries to the upstream cluster
  name: max_retries
  type: integer
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-circuit-breaker-schema.json
slug: ambassador-circuit-breaker
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: CircuitBreaker
---
