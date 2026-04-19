---
description: Address schema from Adyen API
layout: schema
name: Address
properties_list:
- description: 'The name of the city. Maximum length: 3000 characters.'
  name: city
  type: string
- description: The two-character ISO-3166-1 alpha-2 country code. For example, **US**. > If you don't know the country or are not collecting the country from the shopper, provide `country` as `ZZ`.
  name: country
  type: string
- description: 'The number or name of the house. Maximum length: 3000 characters.'
  name: houseNumberOrName
  type: string
- description: A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
  name: postalCode
  type: string
- description: The two-character ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada. > Required for the US and Canada.
  name: stateOrProvince
  type: string
- description: 'The name of the street. Maximum length: 3000 characters. > The house number should not be included in this field; it should be separately provided via `houseNumberOrName`.'
  name: street
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-address-schema.json
slug: payments-address
tags:
- Payments
- Financial Services
- Fintech
title: Address
---
