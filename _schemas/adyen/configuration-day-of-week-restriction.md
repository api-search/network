---
description: DayOfWeekRestriction schema from Adyen API
layout: schema
name: DayOfWeekRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: 'List of days of the week. Possible values: **monday**, **tuesday**, **wednesday**, **thursday**, **friday**, **saturday**, **sunday**.'
  name: value
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-day-of-week-restriction-schema.json
slug: configuration-day-of-week-restriction
tags:
- Payments
- Financial Services
- Fintech
title: DayOfWeekRestriction
---
