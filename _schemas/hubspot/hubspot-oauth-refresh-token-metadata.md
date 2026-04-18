---
description: Metadata associated with an OAuth refresh token
layout: schema
name: RefreshTokenMetadata
properties_list:
- description: The refresh token string
  name: token
  type: string
- description: The client ID of the application
  name: client_id
  type: string
- description: The HubSpot portal (hub) ID associated with this token
  name: hub_id
  type: integer
- description: The ID of the user who authorized the token
  name: user_id
  type: integer
- description: The email address of the user who authorized the token
  name: user
  type: string
- description: List of scopes granted to this token
  name: scopes
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-oauth-refresh-token-metadata-schema.json
slug: hubspot-oauth-refresh-token-metadata
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
title: RefreshTokenMetadata
---
