---
description: ''
layout: schema
name: Pricing
properties_list:
- description: The base nightly price in the listing currency.
  name: nightly_price
  type: number
- description: The ISO 4217 currency code for pricing.
  name: currency
  type: string
- description: The one-time cleaning fee charged per reservation.
  name: cleaning_fee
  type: number
- description: The percentage discount for stays of 7 or more nights.
  name: weekly_discount
  type: number
- description: The percentage discount for stays of 28 or more nights.
  name: monthly_discount
  type: number
- description: The additional fee per extra guest beyond the base occupancy.
  name: extra_guest_fee
  type: number
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-pricing-schema.json
slug: airbnb-pricing
tags: []
title: Pricing
---
