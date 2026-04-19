---
description: Integration schema from Ampersand API
layout: schema
name: Integration
properties_list:
- description: The integration ID.
  name: id
  type: string
- description: The Ampersand project ID.
  name: projectId
  type: string
- description: The integration name.
  name: name
  type: string
- description: The SaaS provider that this integration connects to.
  name: provider
  type: string
- description: The time the integration was created.
  name: createTime
  type: string
- description: The time the integration was last updated.
  name: updateTime
  type: string
- description: ''
  name: latestRevision
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-integration-schema.json
slug: ampersand-api-integration
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: Integration
---
