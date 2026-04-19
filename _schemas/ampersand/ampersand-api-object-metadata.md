---
description: ObjectMetadata schema from Ampersand API
layout: schema
name: ObjectMetadata
properties_list:
- description: The provider name of the object
  name: name
  type: string
- description: Human-readable name of the object
  name: displayName
  type: string
- description: The mapped name of the object as defined in your integration config, if a mapping was applied. Only present when using the installation-scoped metadata endpoint.
  name: mappedObjectName
  type: string
- description: Map of field metadata keyed by field name
  name: fields
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-object-metadata-schema.json
slug: ampersand-api-object-metadata
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: ObjectMetadata
---
