---
description: General details about the Kong Gateway node.
layout: schema
name: NodeInfo
properties_list:
- description: The version of the Kong Gateway instance.
  name: version
  type: string
- description: The version of the Lua runtime.
  name: lua_version
  type: string
- description: ''
  name: tagline
  type: string
- description: ''
  name: hostname
  type: string
- description: ''
  name: node_id
  type: string
- description: ''
  name: timers
  type: object
- description: ''
  name: plugins
  type: object
- description: ''
  name: configuration
  type: object
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-node-info-schema.json
slug: kong-gateway-admin-node-info
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: NodeInfo
---
