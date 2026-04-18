---
description: The result of sending a message to a single recipient.
layout: schema
name: SendResult
properties_list:
- description: The recipient email address.
  name: email
  type: string
- description: The sending status for this recipient.
  name: status
  type: string
- description: The reason the message was rejected, if applicable.
  name: reject_reason
  type: string
- description: The reason the message was queued instead of sent immediately.
  name: queued_reason
  type: string
- description: The unique message ID for this recipient's message.
  name: _id
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-send-result-schema.json
slug: mailchimp-transactional-send-result
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: SendResult
---
