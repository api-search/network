---
description: Request body for token creation or refresh
layout: schema
name: TokenRequest
properties_list:
- description: The type of grant being requested
  name: grant_type
  type: string
- description: The client ID of your application
  name: client_id
  type: string
- description: The client secret of your application
  name: client_secret
  type: string
- description: The redirect URI (required for authorization_code grant)
  name: redirect_uri
  type: string
- description: The authorization code (required for authorization_code grant)
  name: code
  type: string
- description: The refresh token (required for refresh_token grant)
  name: refresh_token
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-oauth-token-request-schema.json
slug: hubspot-oauth-token-request
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
title: TokenRequest
---
