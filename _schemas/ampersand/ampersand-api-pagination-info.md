---
description: PaginationInfo schema from Ampersand API
layout: schema
name: PaginationInfo
properties_list:
- description: If set to true, this is the last page of results for the given operation. There are no more results & there will be no nextPageToken sent when done is true.
  name: done
  type: boolean
- description: If present, set this value against your 'pageToken' query parameter in the next API call, which will retrieve the next set of results.
  name: nextPageToken
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-pagination-info-schema.json
slug: ampersand-api-pagination-info
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: PaginationInfo
---
