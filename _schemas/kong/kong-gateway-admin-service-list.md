---
description: A paginated list of Service entities.
layout: schema
name: ServiceList
properties_list:
- description: ''
  name: data
  type: array
- description: URI to the next page of results.
  name: next
  type: string
- description: Offset token for the next page.
  name: offset
  type: string
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-service-list-schema.json
slug: kong-gateway-admin-service-list
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: ServiceList
---
