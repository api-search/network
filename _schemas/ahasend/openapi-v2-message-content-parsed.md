---
description: MessageContentParsed schema from AhaSend API
layout: schema
name: MessageContentParsed
properties_list:
- description: Array of message content parts (text, HTML, etc.)
  name: parts
  type: array
- description: Array of message attachments
  name: attachments
  type: array
- description: Email headers as key-value pairs (values are arrays to handle multiple headers with same name)
  name: headers
  type: object
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-message-content-parsed-schema.json
slug: openapi-v2-message-content-parsed
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: MessageContentParsed
---
