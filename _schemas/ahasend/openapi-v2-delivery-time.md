---
description: DeliveryTime schema from AhaSend API
layout: schema
name: DeliveryTime
properties_list:
- description: The recipient domain
  name: recipient_domain
  type: string
- description: The average time from reception to delivery in seconds
  name: delivery_time
  type: number
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-delivery-time-schema.json
slug: openapi-v2-delivery-time
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: DeliveryTime
---
