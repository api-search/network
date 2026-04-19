---
description: BounceStatistics schema from AhaSend API
layout: schema
name: BounceStatistics
properties_list:
- description: Start time of the statistics bucket
  name: from_timestamp
  type: string
- description: End time of the statistics bucket
  name: to_timestamp
  type: string
- description: Bounce count per bounce classification
  name: bounces
  type: array
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-bounce-statistics-schema.json
slug: openapi-v2-bounce-statistics
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: BounceStatistics
---
