---
description: Information about a subaccount.
layout: schema
name: SubaccountInfo
properties_list:
- description: The unique subaccount identifier.
  name: id
  type: string
- description: The display name of the subaccount.
  name: name
  type: string
- description: Notes about the subaccount.
  name: notes
  type: string
- description: The manual hourly quota, if set.
  name: custom_quota
  type: integer
- description: The current status of the subaccount.
  name: status
  type: string
- description: The subaccount sending reputation (0-100).
  name: reputation
  type: integer
- description: When the subaccount was created.
  name: created_at
  type: string
- description: When the subaccount first sent a message.
  name: first_sent_at
  type: string
- description: Messages sent in the last week.
  name: sent_weekly
  type: integer
- description: Messages sent in the last month.
  name: sent_monthly
  type: integer
- description: Total messages sent.
  name: sent_total
  type: integer
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-subaccount-info-schema.json
slug: mailchimp-transactional-subaccount-info
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: SubaccountInfo
---
