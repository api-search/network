---
description: ProviderApp schema from Ampersand API
layout: schema
name: ProviderApp
properties_list:
- description: The provider app ID.
  name: id
  type: string
- description: The Ampersand project ID.
  name: projectId
  type: string
- description: The ID used by the provider to identify the app (optional).
  name: externalRef
  type: string
- description: The SaaS provider that this app connects to.
  name: provider
  type: string
- description: The OAuth client ID for this app.
  name: clientId
  type: string
- description: The OAuth scopes for this app.
  name: scopes
  type: array
- description: ''
  name: metadata
  type: object
- description: The time the provider app was created.
  name: createTime
  type: string
- description: The time the provider app was updated.
  name: updateTime
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-provider-app-schema.json
slug: ampersand-api-provider-app
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: ProviderApp
---
