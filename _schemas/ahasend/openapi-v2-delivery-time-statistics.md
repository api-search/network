---
description: DeliveryTimeStatistics schema from AhaSend API
layout: schema
name: DeliveryTimeStatistics
properties_list:
- description: Start time of the statistics bucket
  name: from_timestamp
  type: string
- description: End time of the statistics bucket
  name: to_timestamp
  type: string
- description: Average delivery time in seconds
  name: avg_delivery_time
  type: number
- description: Number of messages
  name: delivered_count
  type: integer
- description: ''
  name: delivery_times
  type: array
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-delivery-time-statistics-schema.json
slug: openapi-v2-delivery-time-statistics
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: DeliveryTimeStatistics
---
