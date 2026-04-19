---
description: CreateConversationMessageRequest schema from AhaSend API
layout: schema
name: CreateConversationMessageRequest
properties_list:
- description: ''
  name: from
  type: object
- description: This parameter can set the `To` header to multiple addresses.
  name: to
  type: array
- description: This parameter can set the `CC` header to multiple addresses. Do not include `cc` in the headers array.
  name: cc
  type: array
- description: This parameter can set the `To` header to multiple addresses.
  name: bcc
  type: array
- description: If provided, the reply-to header in headers array must not be provided
  name: reply_to
  type: object
- description: Email subject line
  name: subject
  type: string
- description: Plain text content. Required if html_content is empty
  name: text_content
  type: string
- description: HTML content. Required if text_content is empty
  name: html_content
  type: string
- description: AMP HTML content
  name: amp_content
  type: string
- description: File attachments
  name: attachments
  type: array
- description: Custom email headers. `cc` and `reply-to` headers cannot be provided if `reply_to` or `cc` parameters are provided, message-id will be ignored and automatically generated
  name: headers
  type: object
- description: Tags for categorizing messages
  name: tags
  type: array
- description: If true, the message will be sent to the sandbox environment
  name: sandbox
  type: boolean
- description: The result of the sandbox send
  name: sandbox_result
  type: string
- description: Tracking settings for the message, overrides default account settings
  name: tracking
  type: object
- description: Retention settings for the message, overrides default account settings
  name: retention
  type: object
- description: Schedule for message delivery
  name: schedule
  type: object
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-create-conversation-message-request-schema.json
slug: openapi-v2-create-conversation-message-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: CreateConversationMessageRequest
---
