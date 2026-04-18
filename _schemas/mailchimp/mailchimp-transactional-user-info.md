---
description: Account-level information for the authenticated Mandrill user.
layout: schema
name: UserInfo
properties_list:
- description: The account username.
  name: username
  type: string
- description: When the account was created.
  name: created_at
  type: string
- description: A unique public identifier for the account.
  name: public_id
  type: string
- description: The account sending reputation (0-100).
  name: reputation
  type: integer
- description: The hourly email sending quota.
  name: hourly_quota
  type: integer
- description: The number of messages in the send queue.
  name: backlog
  type: integer
- description: Account-level sending statistics.
  name: stats
  type: object
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-user-info-schema.json
slug: mailchimp-transactional-user-info
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: UserInfo
---
