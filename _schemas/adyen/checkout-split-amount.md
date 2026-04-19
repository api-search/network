---
description: SplitAmount schema from Adyen API
layout: schema
name: SplitAmount
properties_list:
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). By default, this is the original payment currency.
  name: currency
  type: string
- description: The value of the split amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: value
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-split-amount-schema.json
slug: checkout-split-amount
tags:
- Payments
- Financial Services
- Fintech
title: SplitAmount
---
