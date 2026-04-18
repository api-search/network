---
description: The full content of a sent message.
layout: schema
name: MessageContent
properties_list:
- description: Unix timestamp of when the message was sent.
  name: ts
  type: integer
- description: The unique message ID.
  name: _id
  type: string
- description: The sender email address.
  name: from_email
  type: string
- description: The sender display name.
  name: from_name
  type: string
- description: The message subject line.
  name: subject
  type: string
- description: The primary recipient.
  name: to
  type: object
- description: Tags applied to the message.
  name: tags
  type: array
- description: The full message headers.
  name: headers
  type: object
- description: The plain-text body of the message.
  name: text
  type: string
- description: The HTML body of the message.
  name: html
  type: string
- description: File attachments included in the message.
  name: attachments
  type: array
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-message-content-schema.json
slug: mailchimp-transactional-message-content
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: MessageContent
---
