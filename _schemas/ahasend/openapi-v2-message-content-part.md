---
description: MessageContentPart schema from AhaSend API
layout: schema
name: MessageContentPart
properties_list:
- description: MIME content type (e.g., "text/plain", "text/html")
  name: content_type
  type: string
- description: The actual content for this part
  name: content
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-message-content-part-schema.json
slug: openapi-v2-message-content-part
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: MessageContentPart
---
