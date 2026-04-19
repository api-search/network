---
description: Recurring schema from Adyen API
layout: schema
name: Recurring
properties_list:
- description: 'The type of recurring contract to be used. Possible values: * `ONECLICK` – Payment details can be used to initiate a one-click payment, where the shopper enters the [card security code (CVC/CVV)](http'
  name: contract
  type: string
- description: A descriptive name for this detail.
  name: recurringDetailName
  type: string
- description: Date after which no further authorisations shall be performed. Only for 3D Secure 2.
  name: recurringExpiry
  type: string
- description: Minimum number of days between authorisations. Only for 3D Secure 2.
  name: recurringFrequency
  type: string
- description: The name of the token service.
  name: tokenService
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-recurring-schema.json
slug: payments-recurring
tags:
- Payments
- Financial Services
- Fintech
title: Recurring
---
