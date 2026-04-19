---
description: Address schema from Adyen API
layout: schema
name: Address
properties_list:
- description: The name of the city. Required if `stateOrProvince` is provided. If you specify the city, you must also send `postalCode` and `street`.
  name: city
  type: string
- description: The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.
  name: country
  type: string
- description: Postal code. Required if `stateOrProvince` and/or `city` is provided.
  name: postalCode
  type: string
- description: The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. If you specify the state or province, you must also send `city`, `postalCode`, and `street`.
  name: stateOrProvince
  type: string
- description: The name of the street, and the house or building number. Required if `stateOrProvince` and/or `city` is provided.
  name: street
  type: string
- description: The apartment, unit, or suite number.
  name: street2
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-address-schema.json
slug: legal-entity-address
tags:
- Payments
- Financial Services
- Fintech
title: Address
---
