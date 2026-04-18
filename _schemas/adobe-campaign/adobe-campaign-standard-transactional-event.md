---
description: TransactionalEvent from Adobe Campaign API
layout: schema
name: TransactionalEvent
properties_list:
- description: Recipient email address (for email channel).
  name: email
  type: string
- description: Recipient mobile phone (for SMS channel).
  name: mobilePhone
  type: string
- description: Push platform (Apple or Google).
  name: pushPlatform
  type: string
- description: Context data for message personalization. Contains dynamic fields matching the transactional message template.
  name: ctx
  type: object
- description: Optional scheduled send time.
  name: scheduled
  type: string
- description: Optional event expiration time.
  name: expiration
  type: string
provider_name: Adobe Campaign
provider_slug: adobe-campaign
schema_file: json-schema/adobe-campaign-standard-transactional-event-schema.json
slug: adobe-campaign-standard-transactional-event
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
title: TransactionalEvent
---
