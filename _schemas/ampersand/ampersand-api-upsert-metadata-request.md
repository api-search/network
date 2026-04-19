---
description: Request payload for upserting metadata (fields only)
layout: schema
name: UpsertMetadataRequest
properties_list:
- description: The ID that your app uses to identify the group of users for this request.
  name: groupRef
  type: string
- description: Maps object names to field definitions
  name: fields
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-upsert-metadata-request-schema.json
slug: ampersand-api-upsert-metadata-request
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: UpsertMetadataRequest
---
