---
description: Contains the introductory price information for a subscription.
layout: schema
name: IntroductoryPriceInfo
properties_list:
- description: ISO 4217 currency code for the introductory price.
  name: introductoryPriceCurrencyCode
  type: string
- description: Introductory price in micro-units of the currency.
  name: introductoryPriceAmountMicros
  type: string
- description: Introductory price period in ISO 8601 format (e.g., P1W for one week, P1M for one month).
  name: introductoryPricePeriod
  type: string
- description: Number of billing periods the introductory price applies for.
  name: introductoryPriceCycles
  type: integer
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-introductory-price-info-schema.json
slug: google-play-developer-introductory-price-info
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
title: IntroductoryPriceInfo
---
