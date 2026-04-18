---
description: ''
layout: schema
name: UpstreamInput
properties_list:
- description: ''
  name: name
  type: string
- description: ''
  name: algorithm
  type: string
- description: ''
  name: hash_on
  type: string
- description: ''
  name: hash_fallback
  type: string
- description: ''
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
- description: ''
  name: slots
  type: integer
- description: ''
  name: tags
  type: array
- description: ''
  name: host_header
  type: string
- description: ''
  name: use_srv_name
  type: boolean
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-upstream-input-schema.json
slug: kong-gateway-admin-upstream-input
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: UpstreamInput
---
