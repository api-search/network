---
description: Cross-Origin Resource Sharing configuration
layout: schema
name: CORSPolicy
properties_list:
- description: Allowed origins. Use a string for exact match or a regex pattern.
  name: origins
  type: array
- description: Allowed HTTP methods
  name: methods
  type: array
- description: Allowed request headers
  name: headers
  type: array
- description: Whether to allow credentials (cookies, authorization headers)
  name: credentials
  type: boolean
- description: Headers exposed to the browser
  name: exposed_headers
  type: array
- description: How long the preflight response can be cached (e.g., '86400')
  name: max_age
  type: string
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-cors-policy-schema.json
slug: ambassador-cors-policy
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: CORSPolicy
---
