---
description: ''
layout: schema
name: TargetInput
properties_list:
- description: The target address (IP or hostname) and port.
  name: target
  type: string
- description: ''
  name: weight
  type: integer
- description: ''
  name: tags
  type: array
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-target-input-schema.json
slug: kong-gateway-admin-target-input
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: TargetInput
---
