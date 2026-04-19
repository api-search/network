---
description: Result of an upsert operation for a single field
layout: schema
name: FieldUpsertResult
properties_list:
- description: Name of the field
  name: fieldName
  type: string
- description: Action taken (create, update, none)
  name: action
  type: string
- description: Provider-specific metadata about the field
  name: metadata
  type: object
- description: Warnings that occurred during the upsert operation
  name: warnings
  type: array
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-field-upsert-result-schema.json
slug: ampersand-api-field-upsert-result
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: FieldUpsertResult
---
