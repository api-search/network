---
description: NameLocation schema from Adyen API
layout: schema
name: NameLocation
properties_list:
- description: The city where the merchant is located.
  name: city
  type: string
- description: The country where the merchant is located in [three-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) format.
  name: country
  type: string
- description: The home country in [three-digit country code](https://en.wikipedia.org/wiki/ISO_3166-1_numeric) format, used for government-controlled merchants such as embassies.
  name: countryOfOrigin
  type: string
- description: The name of the merchant's shop or service.
  name: name
  type: string
- description: The raw data.
  name: rawData
  type: string
- description: The state where the merchant is located.
  name: state
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-name-location-schema.json
slug: accounting-notifications-name-location
tags:
- Payments
- Financial Services
- Fintech
title: NameLocation
---
