---
description: BalanceTransferResponse schema from Adyen API
layout: schema
name: BalanceTransferResponse
properties_list:
- description: The amount of the transfer in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: amount
  type: object
- description: The date when the balance transfer was requested.
  name: createdAt
  type: string
- description: A human-readable description for the transfer. You can use alphanumeric characters and hyphens. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.
  name: description
  type: string
- description: The unique identifier of the source merchant account from which funds are deducted.
  name: fromMerchant
  type: string
- description: Adyen's 16-character string reference associated with the balance transfer.
  name: pspReference
  type: string
- description: 'A reference for the balance transfer. If you don''t provide this in the request, Adyen generates a unique reference. Maximum length: 80 characters.'
  name: reference
  type: string
- description: 'The status of the balance transfer. Possible values: **transferred**, **failed**, **error**, and **notEnoughBalance**.'
  name: status
  type: string
- description: The unique identifier of the destination merchant account from which funds are transferred.
  name: toMerchant
  type: string
- description: 'The type of balance transfer. Possible values: **tax**, **fee**, **terminalSale**, **credit**, **debit**, and **adjustment**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/balance-control-balance-transfer-response-schema.json
slug: balance-control-balance-transfer-response
tags:
- Payments
- Financial Services
- Fintech
title: BalanceTransferResponse
---
