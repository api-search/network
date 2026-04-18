---
description: Metadata associated with an OAuth access token
layout: schema
name: AccessTokenMetadata
properties_list:
- description: The access token string
  name: token
  type: string
- description: The ID of the HubSpot application associated with this token
  name: app_id
  type: integer
- description: The HubSpot portal (hub) ID associated with this token
  name: hub_id
  type: integer
- description: The ID of the user who authorized the token
  name: user_id
  type: integer
- description: The email address of the user who authorized the token
  name: user
  type: string
- description: The domain of the HubSpot portal
  name: hub_domain
  type: string
- description: List of scopes granted to this token
  name: scopes
  type: array
- description: The type of token (always 'access')
  name: token_type
  type: string
- description: Number of seconds until the token expires
  name: expires_in
  type: integer
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/oauth-api-access-token-metadata-schema.json
slug: oauth-api-access-token-metadata
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
title: AccessTokenMetadata
---
