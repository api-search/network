---
description: Balance schema from Adyen API
layout: schema
name: Balance
properties_list:
- description: The remaining amount available for spending.
  name: available
  type: integer
- description: The total amount in the balance.
  name: balance
  type: integer
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance.
  name: currency
  type: string
- description: The amount pending to be paid out but not yet available in the balance.
  name: pending
  type: integer
- description: The amount reserved for payments that have been authorised, but have not been captured yet.
  name: reserved
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-balance-schema.json
slug: configuration-webhooks-balance
tags:
- Payments
- Financial Services
- Fintech
title: Balance
---
