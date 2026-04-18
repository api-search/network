---
description: Input schema for creating or updating a Plugin.
layout: schema
name: PluginInput
properties_list:
- description: The name of the plugin.
  name: name
  type: string
- description: ''
  name: instance_name
  type: string
- description: ''
  name: config
  type: object
- description: ''
  name: protocols
  type: array
- description: ''
  name: enabled
  type: boolean
- description: ''
  name: tags
  type: array
- description: ''
  name: ordering
  type: object
- description: ''
  name: service
  type: object
- description: ''
  name: route
  type: object
- description: ''
  name: consumer
  type: object
- description: ''
  name: consumer_group
  type: object
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-plugin-input-schema.json
slug: kong-gateway-admin-plugin-input
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: PluginInput
---
