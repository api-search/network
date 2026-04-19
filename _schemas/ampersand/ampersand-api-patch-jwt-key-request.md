---
description: PatchJWTKeyRequest schema from Ampersand API
layout: schema
name: PatchJWTKeyRequest
properties_list:
- description: List of field paths to update (currently supports 'active' and 'name')
  name: updateMask
  type: array
- description: Object containing the fields to update with their new values
  name: jwtKey
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-patch-jwt-key-request-schema.json
slug: ampersand-api-patch-jwt-key-request
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: PatchJWTKeyRequest
---
