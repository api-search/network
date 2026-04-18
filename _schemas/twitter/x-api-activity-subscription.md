---
description: An XActivity subscription.
layout: schema
name: ActivitySubscription
properties_list:
- description: ''
  name: created_at
  type: string
- description: ''
  name: event_type
  type: string
- description: An XAA subscription filter.
  name: filter
  type: object
- description: The unique identifier of this subscription.
  name: subscription_id
  type: string
- description: ''
  name: tag
  type: string
- description: ''
  name: updated_at
  type: string
- description: The unique identifier of this webhook config.
  name: webhook_id
  type: string
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-activity-subscription-schema.json
slug: x-api-activity-subscription
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: ActivitySubscription
---
