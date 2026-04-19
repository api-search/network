---
description: DeliveryEvent schema from AhaSend API
layout: schema
name: DeliveryEvent
properties_list:
- description: Timestamp of the delivery event
  name: time
  type: string
- description: Log message for the delivery event
  name: log
  type: string
- description: Status of the delivery event
  name: status
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-delivery-event-schema.json
slug: openapi-v2-delivery-event
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: DeliveryEvent
---
