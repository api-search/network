---
description: Currency schema from Adyen API
layout: schema
name: Currency
properties_list:
- description: Surcharge amount per transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: amount
  type: integer
- description: Three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). For example, **AUD**.
  name: currencyCode
  type: string
- description: Surcharge percentage per transaction. The maximum number of decimal places is two. For example, **1%** or **2.27%**.
  name: percentage
  type: number
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-currency-schema.json
slug: management-currency
tags:
- Payments
- Financial Services
- Fintech
title: Currency
---
