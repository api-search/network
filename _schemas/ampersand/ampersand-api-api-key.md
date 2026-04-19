---
description: ApiKey schema from Ampersand API
layout: schema
name: ApiKey
properties_list:
- description: The API key.
  name: key
  type: string
- description: A short name for the API key.
  name: label
  type: string
- description: ''
  name: scopes
  type: object
- description: The project ID.
  name: projectId
  type: string
- description: Whether the API key is active.
  name: active
  type: boolean
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-api-key-schema.json
slug: ampersand-api-api-key
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: ApiKey
---
