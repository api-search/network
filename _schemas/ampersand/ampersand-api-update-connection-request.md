---
description: Specify which fields to update in `updateMask` and provide corresponding values in `connection`. Fields in `connection` not listed in `updateMask` are ignored.
layout: schema
name: UpdateConnectionRequest
properties_list:
- description: Fields to update. Each entry must have a corresponding value in `connection`. Credential fields (`apiKey`, `basicAuth`, `oauth2ClientCredentials`, `oauth2PasswordCredentials`) must match the connectio
  name: updateMask
  type: array
- description: ''
  name: connection
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-update-connection-request-schema.json
slug: ampersand-api-update-connection-request
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: UpdateConnectionRequest
---
