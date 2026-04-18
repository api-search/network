---
description: Information and statistics for a message tag.
layout: schema
name: TagInfo
properties_list:
- description: The tag name.
  name: tag
  type: string
- description: The reputation score for the tag (0-100).
  name: reputation
  type: integer
- description: Total number of messages sent with this tag.
  name: sent
  type: integer
- description: Total hard bounces for messages with this tag.
  name: hard_bounces
  type: integer
- description: Total soft bounces for messages with this tag.
  name: soft_bounces
  type: integer
- description: Total rejects for messages with this tag.
  name: rejects
  type: integer
- description: Total spam complaints for messages with this tag.
  name: complaints
  type: integer
- description: Total unsubscribes for messages with this tag.
  name: unsubs
  type: integer
- description: Total opens for messages with this tag.
  name: opens
  type: integer
- description: Total clicks for messages with this tag.
  name: clicks
  type: integer
- description: Unique opens for messages with this tag.
  name: unique_opens
  type: integer
- description: Unique clicks for messages with this tag.
  name: unique_clicks
  type: integer
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-tag-info-schema.json
slug: mailchimp-transactional-tag-info
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: TagInfo
---
