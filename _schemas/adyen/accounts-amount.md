---
description: Amount schema from Adyen API
layout: schema
name: Amount
properties_list:
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes).
  name: currency
  type: string
- description: The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: value
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-amount-schema.json
slug: accounts-amount
tags:
- Payments
- Financial Services
- Fintech
title: Amount
---
