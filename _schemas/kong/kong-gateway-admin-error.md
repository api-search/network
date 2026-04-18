---
description: Standard error response from the Admin API.
layout: schema
name: Error
properties_list:
- description: A human-readable error message.
  name: message
  type: string
- description: The error type name.
  name: name
  type: string
- description: An optional error code.
  name: code
  type: integer
- description: Field-level validation errors.
  name: fields
  type: object
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-error-schema.json
slug: kong-gateway-admin-error
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: Error
---
