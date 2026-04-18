---
description: An Upstream object represents a virtual hostname and can be used to health-check, circuit-break, and load-balance incoming requests over multiple services.
layout: schema
name: Upstream
properties_list:
- description: ''
  name: id
  type: string
- description: A hostname which must be equal to the host of a Service.
  name: name
  type: string
- description: The load balancing algorithm to use.
  name: algorithm
  type: string
- description: What to use as hashing input when the consistent-hashing algorithm is selected.
  name: hash_on
  type: string
- description: What to use as hashing input if the primary hash_on does not return a hash.
  name: hash_fallback
  type: string
- description: The header name to take the value from as hash input (when hash_on is set to header).
  name: hash_on_header
  type: string
- description: ''
  name: hash_fallback_header
  type: string
- description: ''
  name: hash_on_cookie
  type: string
- description: ''
  name: hash_on_cookie_path
  type: string
- description: ''
  name: hash_on_query_arg
  type: string
- description: ''
  name: hash_fallback_query_arg
  type: string
- description: ''
  name: hash_on_uri_capture
  type: string
- description: ''
  name: hash_fallback_uri_capture
  type: string
- description: The number of slots in the load balancer algorithm.
  name: slots
  type: integer
- description: ''
  name: tags
  type: array
- description: The hostname to be used as Host header when proxying requests through ring-balancer.
  name: host_header
  type: string
- description: If set, balancer will use SRV hostname as the proxy Host header.
  name: use_srv_name
  type: boolean
- description: ''
  name: created_at
  type: integer
- description: ''
  name: updated_at
  type: integer
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-upstream-schema.json
slug: kong-gateway-admin-upstream
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: Upstream
---
