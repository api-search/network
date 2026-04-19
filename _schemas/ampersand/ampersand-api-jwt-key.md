---
description: JWTKey schema from Ampersand API
layout: schema
name: JWTKey
properties_list:
- description: Unique identifier for the JWT key
  name: id
  type: string
- description: The project this JWT key belongs to
  name: projectId
  type: string
- description: Human-readable name for the JWT key
  name: label
  type: string
- description: The cryptographic algorithm used
  name: algorithm
  type: string
- description: RSA public key in PEM format
  name: publicKeyPem
  type: string
- description: Whether the JWT key is currently active and can be used for verification
  name: active
  type: boolean
- description: Timestamp when the JWT key was created
  name: createTime
  type: string
- description: Timestamp when the JWT key was last updated
  name: updateTime
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-jwt-key-schema.json
slug: ampersand-api-jwt-key
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: JWTKey
---
