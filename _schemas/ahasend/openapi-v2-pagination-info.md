---
description: PaginationInfo schema from AhaSend API
layout: schema
name: PaginationInfo
properties_list:
- description: Whether there are more items available
  name: has_more
  type: boolean
- description: Cursor for the next page of results
  name: next_cursor
  type: string
- description: Cursor for the previous page of results
  name: previous_cursor
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-pagination-info-schema.json
slug: openapi-v2-pagination-info
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: PaginationInfo
---
