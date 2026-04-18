---
description: Information and statistics for a sender address.
layout: schema
name: SenderInfo
properties_list:
- description: The sender email address.
  name: address
  type: string
- description: When the sender was first used.
  name: created_at
  type: string
- description: Total number of messages sent from this address.
  name: sent
  type: integer
- description: Total hard bounces.
  name: hard_bounces
  type: integer
- description: Total soft bounces.
  name: soft_bounces
  type: integer
- description: Total rejects.
  name: rejects
  type: integer
- description: Total spam complaints.
  name: complaints
  type: integer
- description: Total unsubscribes.
  name: unsubs
  type: integer
- description: Total opens.
  name: opens
  type: integer
- description: Total clicks.
  name: clicks
  type: integer
- description: Unique opens.
  name: unique_opens
  type: integer
- description: Unique clicks.
  name: unique_clicks
  type: integer
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-sender-info-schema.json
slug: mailchimp-transactional-sender-info
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: SenderInfo
---
