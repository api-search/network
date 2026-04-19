---
description: Split schema from Adyen API
layout: schema
name: Split
properties_list:
- description: The unique identifier of the account to which the split amount is booked. Required if `type` is **MarketPlace** or **BalanceAccount**. * [Classic Platforms integration](https://docs.adyen.com/marketpl
  name: account
  type: string
- description: The amount of the split item. * Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic). * Required if `type` is **BalanceAccount
  name: amount
  type: object
- description: Your description for the split item.
  name: description
  type: string
- description: Your unique reference for the split item. This is required if `type` is **MarketPlace** ([Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic)) or **BalanceAccount
  name: reference
  type: string
- description: 'The type of the split item. Possible values: * [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic): **Commission**, **Default**, **Marketplace**, **PaymentFee**,'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-split-schema.json
slug: checkout-split
tags:
- Payments
- Financial Services
- Fintech
title: Split
---
