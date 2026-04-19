---
description: ViasAddress schema from Adyen API
layout: schema
name: ViasAddress
properties_list:
- description: The name of the city. Required if the `houseNumberOrName`, `street`, `postalCode`, or `stateOrProvince` are provided.
  name: city
  type: string
- description: The two-character country code of the address in ISO-3166-1 alpha-2 format. For example, **NL**.
  name: country
  type: string
- description: The number or name of the house.
  name: houseNumberOrName
  type: string
- description: 'The postal code. Required if the `houseNumberOrName`, `street`, `city`, or `stateOrProvince` are provided. Maximum length: * 5 digits for addresses in the US. * 10 characters for all other countries.'
  name: postalCode
  type: string
- description: 'The abbreviation of the state or province. Required if the `houseNumberOrName`, `street`, `city`, or `postalCode` are provided. Maximum length: * 2 characters for addresses in the US or Canada. * 3 ch'
  name: stateOrProvince
  type: string
- description: The name of the street. Required if the `houseNumberOrName`, `city`, `postalCode`, or `stateOrProvince` are provided.
  name: street
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-vias-address-schema.json
slug: notifications-vias-address
tags:
- Payments
- Financial Services
- Fintech
title: ViasAddress
---
