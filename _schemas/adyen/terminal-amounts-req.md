---
description: Amounts of a payment
layout: schema
name: AmountsReq
properties_list:
- description: ''
  name: Currency
  type: string
- description: ''
  name: RequestedAmount
  type: number
- description: ''
  name: CashBackAmount
  type: number
- description: ''
  name: TipAmount
  type: number
- description: ''
  name: PaidAmount
  type: number
- description: ''
  name: MinimumAmountToDeliver
  type: number
- description: ''
  name: MaximumCashBackAmount
  type: number
- description: ''
  name: MinimumSplitAmount
  type: number
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-amounts-req-schema.json
slug: terminal-amounts-req
tags:
- Payments
- Financial Services
- Fintech
title: AmountsReq
---
