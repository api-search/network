---
description: Config schema from Ampersand API
layout: schema
name: Config
properties_list:
- description: The config ID.
  name: id
  type: string
- description: The ID of the revision that was current when this config was created or last updated.
  name: revisionId
  type: string
- description: The time the config was created.
  name: createTime
  type: string
- description: The person who created the config, in the format of "consumer:{consumer-id}" or "builder:{builder-id}".
  name: createdBy
  type: string
- description: ''
  name: content
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-config-schema.json
slug: ampersand-api-config
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: Config
---
