---
description: Conditions on which the transaction must be processed.
layout: schema
name: TransactionConditions
properties_list:
- description: ''
  name: AllowedPaymentBrand
  type: array
- description: ''
  name: AcquirerID
  type: array
- description: The preferred type of payment is a debit transaction rather a credit transaction.
  name: DebitPreferredFlag
  type: boolean
- description: ''
  name: AllowedLoyaltyBrand
  type: array
- description: ''
  name: LoyaltyHandling
  type: object
- description: If the language is selected by the Sale System before the request to the POI.
  name: CustomerLanguage
  type: string
- description: Go online if data sent.
  name: ForceOnlineFlag
  type: boolean
- description: ''
  name: ForceEntryMode
  type: object
- description: The payment implies a specific MCC.
  name: MerchantCategoryCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-transaction-conditions-schema.json
slug: terminal-transaction-conditions
tags:
- Payments
- Financial Services
- Fintech
title: TransactionConditions
---
