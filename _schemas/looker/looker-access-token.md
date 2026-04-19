---
description: An API access token returned after successful authentication
layout: schema
name: AccessToken
properties_list:
- description: The OAuth2 access token string
  name: access_token
  type: string
- description: Token type, always 'Bearer'
  name: token_type
  type: string
- description: Number of seconds until the token expires
  name: expires_in
  type: integer
- description: Refresh token (not used in API client credential flow)
  name: refresh_token
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-access-token-schema.json
slug: looker-access-token
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: AccessToken
---
