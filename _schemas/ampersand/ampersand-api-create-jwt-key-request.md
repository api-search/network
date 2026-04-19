---
description: CreateJWTKeyRequest schema from Ampersand API
layout: schema
name: CreateJWTKeyRequest
properties_list:
- description: Human-readable label for the JWT key
  name: label
  type: string
- description: The cryptographic JWT signing algorithm (currently only RS256 is supported)
  name: algorithm
  type: string
- description: RSA public key in PEM format for JWT signature verification
  name: publicKeyPem
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-create-jwt-key-request-schema.json
slug: ampersand-api-create-jwt-key-request
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: CreateJWTKeyRequest
---
