---
description: Payment schema from Adyen API
layout: schema
name: Payment
properties_list:
- description: The default currency for contactless payments on the payment terminal, as the three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code.
  name: contactlessCurrency
  type: string
- description: Hides the minor units for the listed [ISO currency codes](https://en.wikipedia.org/wiki/ISO_4217).
  name: hideMinorUnitsInCurrencies
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-payment-schema.json
slug: management-payment
tags:
- Payments
- Financial Services
- Fintech
title: Payment
---
