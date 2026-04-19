---
description: MessageAttachment schema from AhaSend API
layout: schema
name: MessageAttachment
properties_list:
- description: Original filename of the attachment
  name: filename
  type: string
- description: Base64 encoded attachment content
  name: content
  type: string
- description: MIME content type of the attachment
  name: content_type
  type: string
- description: Content-ID for inline attachments
  name: content_id
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-message-attachment-schema.json
slug: openapi-v2-message-attachment
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: MessageAttachment
---
