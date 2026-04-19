---
description: SplitAmount schema from Adyen API
layout: schema
name: SplitAmount
properties_list:
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). If this value is not provided, the currency in which the payment is made will be used.
  name: currency
  type: string
- description: The amount in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: value
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-split-amount-schema.json
slug: funds-split-amount
tags:
- Payments
- Financial Services
- Fintech
title: SplitAmount
---
