---
description: PaginatedMessagesResponse schema from AhaSend API
layout: schema
name: PaginatedMessagesResponse
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Array of message summaries (content and content_parsed fields omitted for performance)
  name: data
  type: array
- description: ''
  name: pagination
  type: object
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-paginated-messages-response-schema.json
slug: openapi-v2-paginated-messages-response
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: PaginatedMessagesResponse
---
