---
description: Load balancing configuration for an upstream cluster
layout: schema
name: LoadBalancer
properties_list:
- description: Load balancing algorithm
  name: policy
  type: string
- description: Cookie-based session affinity configuration (for ring_hash policy)
  name: cookie
  type: object
- description: Header to use for hash-based load balancing
  name: header
  type: string
- description: Whether to use source IP for hash-based load balancing
  name: source_ip
  type: boolean
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-load-balancer-schema.json
slug: ambassador-load-balancer
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: LoadBalancer
---
