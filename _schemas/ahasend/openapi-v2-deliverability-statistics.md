---
description: DeliverabilityStatistics schema from AhaSend API
layout: schema
name: DeliverabilityStatistics
properties_list:
- description: Start time of the statistics bucket
  name: from_timestamp
  type: string
- description: End time of the statistics bucket
  name: to_timestamp
  type: string
- description: Number of messages accepted for delivery
  name: reception_count
  type: integer
- description: Number of messages delivered
  name: delivered_count
  type: integer
- description: Number of messages deferred
  name: deferred_count
  type: integer
- description: Number of messages bounced
  name: bounced_count
  type: integer
- description: Number of messages failed
  name: failed_count
  type: integer
- description: Number of messages suppressed
  name: suppressed_count
  type: integer
- description: Number of messages opened at least once
  name: opened_count
  type: integer
- description: Number of messages that have at least one link in them clicked.
  name: clicked_count
  type: integer
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-deliverability-statistics-schema.json
slug: openapi-v2-deliverability-statistics
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: DeliverabilityStatistics
---
