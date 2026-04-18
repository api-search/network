---
description: A Target is an IP address/hostname with a port that identifies an instance of a backend service.
layout: schema
name: Target
properties_list:
- description: ''
  name: id
  type: string
- description: The target address (IP or hostname) and port (host:port).
  name: target
  type: string
- description: The weight this target gets within the upstream (0-65535). 0 means the target is disabled.
  name: weight
  type: integer
- description: ''
  name: tags
  type: array
- description: ''
  name: upstream
  type: object
- description: ''
  name: created_at
  type: number
- description: ''
  name: updated_at
  type: number
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-target-schema.json
slug: kong-gateway-admin-target
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: Target
---
