---
description: A Service entity represents an upstream API or microservice that Kong Gateway forwards requests to.
layout: schema
name: Service
properties_list:
- description: The unique identifier of the Service.
  name: id
  type: string
- description: An optional human-readable name for the Service.
  name: name
  type: string
- description: The protocol used to communicate with the upstream.
  name: protocol
  type: string
- description: The host of the upstream server.
  name: host
  type: string
- description: The upstream server port.
  name: port
  type: integer
- description: The path to be used in requests to the upstream server.
  name: path
  type: string
- description: The number of retries to execute upon failure to proxy.
  name: retries
  type: integer
- description: The timeout in milliseconds for establishing a connection to the upstream server.
  name: connect_timeout
  type: integer
- description: The timeout in milliseconds between two successive write operations for transmitting a request to the upstream server.
  name: write_timeout
  type: integer
- description: The timeout in milliseconds between two successive read operations for receiving a request from the upstream server.
  name: read_timeout
  type: integer
- description: Shorthand attribute to set protocol, host, port, and path at once. Write-only convenience field.
  name: url
  type: string
- description: An optional set of strings for grouping and filtering.
  name: tags
  type: array
- description: Certificate to be used as client certificate while TLS handshaking to the upstream server.
  name: client_certificate
  type: object
- description: Whether to enable TLS verification of upstream server certificate.
  name: tls_verify
  type: boolean
- description: Maximum depth of chain while verifying upstream server TLS certificate.
  name: tls_verify_depth
  type: integer
- description: Array of CA Certificate object UUIDs used to verify upstream server TLS certificate.
  name: ca_certificates
  type: array
- description: Whether the Service is active.
  name: enabled
  type: boolean
- description: Unix epoch timestamp of when the entity was created.
  name: created_at
  type: integer
- description: Unix epoch timestamp of when the entity was last updated.
  name: updated_at
  type: integer
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-service-schema.json
slug: kong-gateway-admin-service
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: Service
---
