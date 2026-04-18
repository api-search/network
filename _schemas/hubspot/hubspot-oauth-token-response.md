---
description: Response containing the new access token and related information
layout: schema
name: TokenResponse
properties_list:
- description: The new access token
  name: access_token
  type: string
- description: The type of token (always 'bearer')
  name: token_type
  type: string
- description: Number of seconds until the access token expires
  name: expires_in
  type: integer
- description: The refresh token for obtaining new access tokens
  name: refresh_token
  type: string
- description: The ID token (only returned if openid scope was requested)
  name: id_token
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-oauth-token-response-schema.json
slug: hubspot-oauth-token-response
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: TokenResponse
---
