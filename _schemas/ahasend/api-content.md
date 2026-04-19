---
description: Content schema from AhaSend API
layout: schema
name: Content
properties_list:
- description: ''
  name: subject
  type: string
- description: Plaintext body of the email
  name: text_body
  type: string
- description: HTML body of the email
  name: html_body
  type: string
- description: ''
  name: attachments
  type: array
- description: ''
  name: reply_to
  type: object
- description: Specify arbitary headers.
  name: headers
  type: object
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/api-content-schema.json
slug: api-content
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Content
---
