---
description: Represents a monetary amount with currency.
layout: schema
name: Money
properties_list:
- description: ISO 4217 three-letter currency code (e.g., USD, EUR).
  name: currencyCode
  type: string
- description: The whole units of the amount.
  name: units
  type: string
- description: Number of nano units (10^-9) of the amount. Must be between -999,999,999 and +999,999,999.
  name: nanos
  type: integer
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-money-schema.json
slug: google-play-developer-money
tags:
- AI
- Android
- Automotive
- Google
- Machine Learning
- Mobile Development
- SDK
- TV
- Wearables
title: Money
---
