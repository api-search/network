---
description: Attachment schema from AhaSend API
layout: schema
name: Attachment
properties_list:
- description: The attachment data. If the base64 field is true, this data must be encoded using base64. Otherwise, it will be interpreted as UTF-8.
  name: data
  type: string
- description: If set to true, data needs to be encoded using base64. Otherwise data will be interpreted as UTF-8.
  name: base64
  type: boolean
- description: ''
  name: content_type
  type: string
- description: If specified, this attachment will be added as an inline attachment and a multipart/related MIME container will be generated in the message to hold it and the textual content.
  name: content_id
  type: string
- description: ''
  name: file_name
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/api-attachment-schema.json
slug: api-attachment
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Attachment
---
