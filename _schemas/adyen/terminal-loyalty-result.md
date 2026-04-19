---
description: In the Message Response, the result of each loyalty brand transaction. Data related to the result of a processed loyalty transaction.
layout: schema
name: LoyaltyResult
properties_list:
- description: ''
  name: LoyaltyAccount
  type: object
- description: if known (provided by the card or an external host).
  name: CurrentBalance
  type: number
- description: ''
  name: LoyaltyAmount
  type: object
- description: ''
  name: LoyaltyAcquirerData
  type: object
- description: ''
  name: Rebates
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-loyalty-result-schema.json
slug: terminal-loyalty-result
tags:
- Payments
- Financial Services
- Fintech
title: LoyaltyResult
---
