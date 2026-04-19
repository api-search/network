---
description: CapitalBalance schema from Adyen API
layout: schema
name: CapitalBalance
properties_list:
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes).
  name: currency
  type: string
- description: Fee amount.
  name: fee
  type: integer
- description: Principal amount.
  name: principal
  type: integer
- description: Total amount. A sum of principal amount and fee amount.
  name: total
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-capital-balance-schema.json
slug: configuration-capital-balance
tags:
- Payments
- Financial Services
- Fintech
title: CapitalBalance
---
