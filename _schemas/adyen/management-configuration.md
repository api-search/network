---
description: Configuration schema from Adyen API
layout: schema
name: Configuration
properties_list:
- description: Payment method, like **eftpos_australia** or **mc**. See the [possible values](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api).
  name: brand
  type: string
- description: Countries, to filter different surcharge amounts for domestic or international cards.
  name: country
  type: array
- description: Currency, and surcharge percentage or amount.
  name: currencies
  type: array
- description: 'Funding source. Possible values: * **Credit** * **Debit**'
  name: sources
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-configuration-schema.json
slug: management-configuration
tags:
- Payments
- Financial Services
- Fintech
title: Configuration
---
