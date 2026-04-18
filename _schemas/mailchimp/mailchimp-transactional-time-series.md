---
description: An hourly time series data point with sending statistics.
layout: schema
name: TimeSeries
properties_list:
- description: The hour this data point covers (UTC).
  name: time
  type: string
- description: Number of messages sent.
  name: sent
  type: integer
- description: Number of hard bounces.
  name: hard_bounces
  type: integer
- description: Number of soft bounces.
  name: soft_bounces
  type: integer
- description: Number of rejects.
  name: rejects
  type: integer
- description: Number of spam complaints.
  name: complaints
  type: integer
- description: Number of unsubscribes.
  name: unsubs
  type: integer
- description: Number of opens.
  name: opens
  type: integer
- description: Number of unique opens.
  name: unique_opens
  type: integer
- description: Number of clicks.
  name: clicks
  type: integer
- description: Number of unique clicks.
  name: unique_clicks
  type: integer
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-time-series-schema.json
slug: mailchimp-transactional-time-series
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: TimeSeries
---
