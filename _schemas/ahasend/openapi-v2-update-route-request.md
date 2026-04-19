---
description: UpdateRouteRequest schema from AhaSend API
layout: schema
name: UpdateRouteRequest
properties_list:
- description: Route name
  name: name
  type: string
- description: Webhook URL for the route
  name: url
  type: string
- description: Recipient filter
  name: recipient
  type: string
- description: Whether to include attachments in webhooks
  name: attachments
  type: boolean
- description: Whether to include headers in webhooks
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
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-update-route-request-schema.json
slug: openapi-v2-update-route-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: UpdateRouteRequest
---
