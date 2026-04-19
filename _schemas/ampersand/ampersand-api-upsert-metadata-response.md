---
description: Response containing results for all created/updated fields
layout: schema
name: UpsertMetadataResponse
properties_list:
- description: Indicates if the upsert operation was successful
  name: success
  type: boolean
- description: Maps object name -> field name -> upsert result
  name: fields
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-upsert-metadata-response-schema.json
slug: ampersand-api-upsert-metadata-response
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: UpsertMetadataResponse
---
