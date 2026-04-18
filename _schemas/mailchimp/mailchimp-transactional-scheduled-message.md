---
description: A message scheduled for future delivery.
layout: schema
name: ScheduledMessage
properties_list:
- description: The unique scheduled message ID.
  name: _id
  type: string
- description: When the scheduled message was created.
  name: created_at
  type: string
- description: When the message is scheduled to be sent.
  name: send_at
  type: string
- description: The sender email address.
  name: from_email
  type: string
- description: The recipient email address.
  name: to
  type: string
- description: The message subject line.
  name: subject
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-scheduled-message-schema.json
slug: mailchimp-transactional-scheduled-message
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: ScheduledMessage
---
