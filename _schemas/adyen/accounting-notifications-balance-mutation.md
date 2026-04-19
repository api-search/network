---
description: BalanceMutation schema from Adyen API
layout: schema
name: BalanceMutation
properties_list:
- description: The amount in the payment's currency that is debited or credited on the balance accounting register.
  name: balance
  type: integer
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes).
  name: currency
  type: string
- description: The amount in the payment's currency that is debited or credited on the received accounting register.
  name: received
  type: integer
- description: The amount in the payment's currency that is debited or credited on the reserved accounting register.
  name: reserved
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-balance-mutation-schema.json
slug: accounting-notifications-balance-mutation
tags:
- Payments
- Financial Services
- Fintech
title: BalanceMutation
---
