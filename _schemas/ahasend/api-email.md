---
description: Email schema from AhaSend API
layout: schema
name: Email
properties_list:
- description: ''
  name: from
  type: object
- description: Specifies the list of recipients to which message will be sent.
  name: recipients
  type: array
- description: ''
  name: content
  type: object
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/api-email-schema.json
slug: api-email
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Email
---
