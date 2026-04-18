---
description: ''
layout: schema
name: Address
properties_list:
- description: The first line of the street part in the structured address.
  name: addressLine1
  type: string
- description: The second line of the street part in the structured address.
  name: addressLine2
  type: string
- description: The name of the city in the structured address.
  name: addressCity
  type: string
- description: The state/province/parent subdivision code of the structured address.
  name: addressState
  type: string
- description: The postal code of the structured address.
  name: addressPostCode
  type: string
- description: 'The ISO-3166-1 numeric country code of the billing or shipping address requested by the cardholder. See: [ISO-3166](https://www.nationsonline.org/oneworld/country_code_list.htm).'
  name: addressCountry
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-address-schema.json
slug: mastercard-identity-insights-for-transactions-address
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Address
---
