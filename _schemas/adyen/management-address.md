---
description: Address schema from Adyen API
layout: schema
name: Address
properties_list:
- description: The name of the city.
  name: city
  type: string
- description: The name of the company.
  name: companyName
  type: string
- description: The two-letter country code, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format.
  name: country
  type: string
- description: The postal code.
  name: postalCode
  type: string
- description: 'The state or province as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada. Applicable for the following countries: - Australia - Brazil - Canad'
  name: stateOrProvince
  type: string
- description: The name of the street, and the house or building number.
  name: streetAddress
  type: string
- description: Additional address details, if any.
  name: streetAddress2
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-address-schema.json
slug: management-address
tags:
- Payments
- Financial Services
- Fintech
title: Address
---
