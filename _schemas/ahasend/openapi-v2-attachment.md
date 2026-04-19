---
description: Attachment schema from AhaSend API
layout: schema
name: Attachment
properties_list:
- description: If true, data must be encoded using base64. Otherwise, data will be interpreted as UTF-8
  name: base64
  type: boolean
- description: Either plaintext or base64 encoded attachment data (depending on base64 field)
  name: data
  type: string
- description: The MIME type of the attachment
  name: content_type
  type: string
- description: The disposition of the attachment
  name: content_disposition
  type: string
- description: The Content-ID of the attachment for inline images
  name: content_id
  type: string
- description: The filename of the attachment
  name: file_name
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-attachment-schema.json
slug: openapi-v2-attachment
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Attachment
---
