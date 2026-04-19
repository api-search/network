---
description: CardAcquisitionTransaction schema from Adyen API
layout: schema
name: CardAcquisitionTransaction
properties_list:
- description: ''
  name: AllowedPaymentBrand
  type: array
- description: ''
  name: AllowedLoyaltyBrand
  type: array
- description: ''
  name: LoyaltyHandling
  type: object
- description: ''
  name: CustomerLanguage
  type: string
- description: ''
  name: ForceEntryMode
  type: object
- description: ''
  name: ForceCustomerSelectionFlag
  type: boolean
- description: ''
  name: TotalAmount
  type: number
- description: ''
  name: PaymentType
  type: object
- description: ''
  name: CashBackFlag
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-card-acquisition-transaction-schema.json
slug: terminal-card-acquisition-transaction
tags:
- Payments
- Financial Services
- Fintech
title: CardAcquisitionTransaction
---
