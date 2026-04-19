---
description: CountriesRestriction schema from Adyen API
layout: schema
name: CountriesRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: List of two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes.
  name: value
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-countries-restriction-schema.json
slug: configuration-countries-restriction
tags:
- Payments
- Financial Services
- Fintech
title: CountriesRestriction
---
