---
description: Aggregate sending statistics for a time period.
layout: schema
name: AccountStats
properties_list:
- description: Total messages sent.
  name: sent
  type: integer
- description: Total hard bounces.
  name: hard_bounces
  type: integer
- description: Total soft bounces.
  name: soft_bounces
  type: integer
- description: Total rejections.
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
- description: Unique opens.
  name: unique_opens
  type: integer
- description: Total clicks.
  name: clicks
  type: integer
- description: Unique clicks.
  name: unique_clicks
  type: integer
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-account-stats-schema.json
slug: mailchimp-transactional-account-stats
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: AccountStats
---
