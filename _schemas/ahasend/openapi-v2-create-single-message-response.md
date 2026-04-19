---
description: CreateSingleMessageResponse schema from AhaSend API
layout: schema
name: CreateSingleMessageResponse
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Message ID (null if the message was not sent)
  name: id
  type: string
- description: ''
  name: recipient
  type: object
- description: Status of the message
  name: status
  type: string
- description: Error message if the message was not sent
  name: error
  type: string
- description: Provided if the request contained a schedule
  name: schedule
  type: object
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-create-single-message-response-schema.json
slug: openapi-v2-create-single-message-response
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: CreateSingleMessageResponse
---
