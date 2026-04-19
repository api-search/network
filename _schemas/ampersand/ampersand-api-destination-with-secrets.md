---
description: Destination object with secrets field (returned by getDestination when includeSecrets is true)
layout: schema
name: DestinationWithSecrets
properties_list:
- description: The destination ID.
  name: id
  type: string
- description: User-defined name for the destination
  name: name
  type: string
- description: The type of the destination
  name: type
  type: string
- description: ''
  name: metadata
  type: object
- description: The time the destination was created.
  name: createTime
  type: string
- description: The time the destination was updated.
  name: updateTime
  type: string
- description: Destination secrets (only included when includeSecrets is true)
  name: secrets
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-destination-with-secrets-schema.json
slug: ampersand-api-destination-with-secrets
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: DestinationWithSecrets
---
