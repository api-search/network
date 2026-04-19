---
description: CreateMessageRequest schema from AhaSend API
layout: schema
name: CreateMessageRequest
properties_list:
- description: ''
  name: from
  type: object
- description: This does not set the To header to multiple addresses, it sends a separate message for each recipient
  name: recipients
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
- description: Custom email headers. reply-to header cannot be provided if reply_to is provided, message-id will be ignored and automatically generated
  name: headers
  type: object
- description: Global substitutions, recipient substitutions override global
  name: substitutions
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
schema_file: json-schema/openapi-v2-create-message-request-schema.json
slug: openapi-v2-create-message-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: CreateMessageRequest
---
