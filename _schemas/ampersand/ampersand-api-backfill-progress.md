---
description: BackfillProgress schema from Ampersand API
layout: schema
name: BackfillProgress
properties_list:
- description: The installation ID.
  name: installationId
  type: string
- description: The object being synced (e.g., contact, account).
  name: objectName
  type: string
- description: The ID of the backfill operation.
  name: operationId
  type: string
- description: The number of records processed so far. Updates as more records are read during the backfill.
  name: recordsProcessed
  type: integer
- description: The estimated total number of records to process. Only present for Salesforce and HubSpot; other connectors omit this field.
  name: recordsEstimatedTotal
  type: integer
- description: When the backfill operation started.
  name: createTime
  type: string
- description: When progress was last updated.
  name: updateTime
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-backfill-progress-schema.json
slug: ampersand-api-backfill-progress
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: BackfillProgress
---
