---
description: Input schema for creating or updating a Service.
layout: schema
name: ServiceInput
properties_list:
- description: An optional human-readable name for the Service.
  name: name
  type: string
- description: ''
  name: protocol
  type: string
- description: The host of the upstream server.
  name: host
  type: string
- description: ''
  name: port
  type: integer
- description: ''
  name: path
  type: string
- description: ''
  name: retries
  type: integer
- description: ''
  name: connect_timeout
  type: integer
- description: ''
  name: write_timeout
  type: integer
- description: ''
  name: read_timeout
  type: integer
- description: Shorthand attribute to set protocol, host, port, and path at once.
  name: url
  type: string
- description: ''
  name: tags
  type: array
- description: ''
  name: client_certificate
  type: object
- description: ''
  name: tls_verify
  type: boolean
- description: ''
  name: tls_verify_depth
  type: integer
- description: ''
  name: ca_certificates
  type: array
- description: ''
  name: enabled
  type: boolean
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-service-input-schema.json
slug: kong-gateway-admin-service-input
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: ServiceInput
---
