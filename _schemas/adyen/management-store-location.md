---
description: StoreLocation schema from Adyen API
layout: schema
name: StoreLocation
properties_list:
- description: The name of the city.
  name: city
  type: string
- description: The two-letter country code in [ISO_3166-1_alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format.
  name: country
  type: string
- description: The street address.
  name: line1
  type: string
- description: Second address line.
  name: line2
  type: string
- description: Third address line.
  name: line3
  type: string
- description: The postal code.
  name: postalCode
  type: string
- description: 'The state or province code as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada. Required for the following countries: - Australia - Brazil - Ca'
  name: stateOrProvince
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-store-location-schema.json
slug: management-store-location
tags:
- Payments
- Financial Services
- Fintech
title: StoreLocation
---
