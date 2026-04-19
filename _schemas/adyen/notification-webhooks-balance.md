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
- description: The amount reserved for payments that have been authorised, but have not been captured yet.
  name: reserved
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-balance-schema.json
slug: notification-webhooks-balance
tags:
- Payments
- Financial Services
- Fintech
title: Balance
---
