---
description: Summary information about a sent message.
layout: schema
name: MessageInfo
properties_list:
- description: The Unix timestamp when the message was sent.
  name: ts
  type: integer
- description: The unique message ID.
  name: _id
  type: string
- description: The sender email address.
  name: sender
  type: string
- description: The template slug used, if any.
  name: template
  type: string
- description: The subject line of the message.
  name: subject
  type: string
- description: The recipient email address.
  name: email
  type: string
- description: Tags applied to the message.
  name: tags
  type: array
- description: The number of times the message was opened.
  name: opens
  type: integer
- description: Detailed open tracking events.
  name: opens_detail
  type: array
- description: The number of link clicks in the message.
  name: clicks
  type: integer
- description: Detailed click tracking events.
  name: clicks_detail
  type: array
- description: The current state of the message.
  name: state
  type: string
- description: Custom metadata attached to the message.
  name: metadata
  type: object
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-message-info-schema.json
slug: mailchimp-transactional-message-info
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: MessageInfo
---
