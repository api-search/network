---
description: OAuth2 token response
layout: schema
name: TokenResponse
properties_list:
- description: JWT access token
  name: access_token
  type: string
- description: ''
  name: token_type
  type: string
- description: Token lifetime in seconds
  name: expires_in
  type: integer
- description: Refresh token for obtaining new access tokens
  name: refresh_token
  type: string
- description: Granted OAuth2 scopes
  name: scope
  type: string
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/account-management-token-response-schema.json
slug: account-management-token-response
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: TokenResponse
---
