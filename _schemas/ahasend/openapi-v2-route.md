---
description: Route schema from AhaSend API
layout: schema
name: Route
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Unique identifier for the route
  name: id
  type: string
- description: When the route was created
  name: created_at
  type: string
- description: When the route was last updated
  name: updated_at
  type: string
- description: Route name
  name: name
  type: string
- description: Webhook URL for the route
  name: url
  type: string
- description: Recipient filter
  name: recipient
  type: string
- description: Whether to include attachments in route payload
  name: attachments
  type: boolean
- description: Whether to include headers in route payload
  name: headers
  type: boolean
- description: Whether to group by message ID
  name: group_by_message_id
  type: boolean
- description: Whether to strip reply content
  name: strip_replies
  type: boolean
- description: Whether the route is enabled
  name: enabled
  type: boolean
- description: Number of successful calls
  name: success_count
  type: integer
- description: Number of unsuccessful calls
  name: error_count
  type: integer
- description: Number of consecutive failed calls
  name: errors_since_last_success
  type: integer
- description: When the route was last called
  name: last_request_at
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-route-schema.json
slug: openapi-v2-route
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Route
---
