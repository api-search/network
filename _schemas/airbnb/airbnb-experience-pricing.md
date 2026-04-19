---
description: ''
layout: schema
name: ExperiencePricing
properties_list:
- description: The price per guest in the specified currency.
  name: price_per_person
  type: number
- description: The ISO 4217 currency code for pricing.
  name: currency
  type: string
- description: Optional group discount configuration.
  name: group_discount
  type: object
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-experience-pricing-schema.json
slug: airbnb-experience-pricing
tags: []
title: ExperiencePricing
---
