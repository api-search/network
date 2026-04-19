---
description: Address-2 schema from Adyen API
layout: schema
name: Address-2
properties_list:
- description: The name of the city.
  name: city
  type: string
- description: The two-character ISO 3166-1 alpha-2 country code. For example, **US**. >If you don't know the country or are not collecting the country from the shopper, provide `country` as `ZZ`.
  name: country
  type: string
- description: First line of the street address.
  name: line1
  type: string
- description: Second line of the street address.
  name: line2
  type: string
- description: 'The postal code. Maximum length: * 5 digits for an address in the US. * 10 characters for an address in all other countries.'
  name: postalCode
  type: string
- description: The two-letter ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada. > Required for the US and Canada.
  name: stateOrProvince
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-address-2-schema.json
slug: accounting-notifications-address-2
tags:
- Payments
- Financial Services
- Fintech
title: Address-2
---
