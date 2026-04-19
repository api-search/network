---
description: BulkAddress schema from Adyen API
layout: schema
name: BulkAddress
properties_list:
- description: The name of the city.
  name: city
  type: string
- description: The name of the company.
  name: company
  type: string
- description: The two-character ISO-3166-1 alpha-2 country code. For example, **US**.
  name: country
  type: string
- description: The email address.
  name: email
  type: string
- description: The house number or name.
  name: houseNumberOrName
  type: string
- description: The full telephone number.
  name: mobile
  type: string
- description: 'The postal code. Maximum length: * 5 digits for addresses in the US. * 10 characters for all other countries.'
  name: postalCode
  type: string
- description: 'The two-letter ISO 3166-2 state or province code. Maximum length: 2 characters for addresses in the US.'
  name: stateOrProvince
  type: string
- description: The streetname of the house.
  name: street
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-bulk-address-schema.json
slug: configuration-webhooks-bulk-address
tags:
- Payments
- Financial Services
- Fintech
title: BulkAddress
---
