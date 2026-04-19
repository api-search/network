---
description: MessageSchedule schema from AhaSend API
layout: schema
name: MessageSchedule
properties_list:
- description: The time to make the first attempt for delivering the message (RFC3339 format)
  name: first_attempt
  type: string
- description: Expire and drop the message if not delivered by this time (RFC3339 format)
  name: expires
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-message-schedule-schema.json
slug: openapi-v2-message-schedule
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: MessageSchedule
---
