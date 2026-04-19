---
description: Duration schema from Adyen API
layout: schema
name: Duration
properties_list:
- description: 'The unit of time. You can only use **minutes** and **hours** if the `interval.type` is **sliding**. Possible values: **minutes**, **hours**, **days**, **weeks**, or **months**'
  name: unit
  type: string
- description: The length of time by the unit. For example, 5 days. The maximum duration is 90 days or an equivalent in other units. For example, 3 months.
  name: value
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-duration-schema.json
slug: configuration-duration
tags:
- Payments
- Financial Services
- Fintech
title: Duration
---
