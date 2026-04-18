---
description: Input schema for creating or updating a Route.
layout: schema
name: RouteInput
properties_list:
- description: ''
  name: name
  type: string
- description: ''
  name: protocols
  type: array
- description: ''
  name: methods
  type: array
- description: ''
  name: hosts
  type: array
- description: ''
  name: paths
  type: array
- description: ''
  name: headers
  type: object
- description: ''
  name: snis
  type: array
- description: ''
  name: sources
  type: array
- description: ''
  name: destinations
  type: array
- description: ''
  name: https_redirect_status_code
  type: integer
- description: ''
  name: regex_priority
  type: integer
- description: ''
  name: strip_path
  type: boolean
- description: ''
  name: path_handling
  type: string
- description: ''
  name: preserve_host
  type: boolean
- description: ''
  name: request_buffering
  type: boolean
- description: ''
  name: response_buffering
  type: boolean
- description: ''
  name: tags
  type: array
- description: ''
  name: service
  type: object
- description: ''
  name: expression
  type: string
- description: ''
  name: priority
  type: integer
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-route-input-schema.json
slug: kong-gateway-admin-route-input
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: RouteInput
---
