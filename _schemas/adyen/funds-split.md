---
description: Split schema from Adyen API
layout: schema
name: Split
properties_list:
- description: Unique identifier of the account where the split amount should be sent. This is required if `type` is **MarketPlace** or **BalanceAccount**.
  name: account
  type: string
- description: The amount of this split.
  name: amount
  type: object
- description: A description of this split.
  name: description
  type: string
- description: Your reference for the split, which you can use to link the split to other operations such as captures and refunds. This is required if `type` is **MarketPlace** or **BalanceAccount**. For the other t
  name: reference
  type: string
- description: 'The type of split. Possible values: **Default**, **PaymentFee**, **VAT**, **Commission**, **MarketPlace**, **BalanceAccount**, **Remainder**, **Surcharge**, **Tip**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-split-schema.json
slug: funds-split
tags:
- Payments
- Financial Services
- Fintech
title: Split
---
