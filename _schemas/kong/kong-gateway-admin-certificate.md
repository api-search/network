---
description: A Certificate object represents a public certificate for TLS termination.
layout: schema
name: Certificate
properties_list:
- description: ''
  name: id
  type: string
- description: PEM-encoded public certificate chain.
  name: cert
  type: string
- description: PEM-encoded private key of the certificate.
  name: key
  type: string
- description: PEM-encoded public certificate chain of the alternate certificate.
  name: cert_alt
  type: string
- description: PEM-encoded private key of the alternate certificate.
  name: key_alt
  type: string
- description: The list of SNI hostnames associated with this certificate.
  name: snis
  type: array
- description: ''
  name: tags
  type: array
- description: ''
  name: created_at
  type: integer
- description: ''
  name: updated_at
  type: integer
provider_name: Kong
provider_slug: kong
schema_file: json-schema/kong-gateway-admin-certificate-schema.json
slug: kong-gateway-admin-certificate
tags:
- API Gateway
- Lua
- NGINX
- Open Source
title: Certificate
---
