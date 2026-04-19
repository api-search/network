---
description: If Result is Success, contains all the totals, classified as required by the Sale in the message request. At least, transaction totals are provided per Acquirer, Acquirer Settlement, and Card Brand. Result of the Sale to POI Reconciliation processing.
layout: schema
name: TransactionTotals
properties_list:
- description: ''
  name: PaymentInstrumentType
  type: object
- description: If available.
  name: AcquirerID
  type: integer
- description: If available.
  name: HostReconciliationID
  type: string
- description: If configured to present totals per card brand, and Response.Result is Success.
  name: CardBrand
  type: string
- description: If requested in the message request.
  name: POIID
  type: string
- description: If requested in the message request.
  name: SaleID
  type: string
- description: If requested in the message request.
  name: OperatorID
  type: string
- description: If requested in the message request.
  name: ShiftNumber
  type: string
- description: If requested in the message request.
  name: TotalsGroupID
  type: string
- description: Currency of a monetary amount.
  name: PaymentCurrency
  type: string
- description: ''
  name: PaymentTotals
  type: array
- description: ''
  name: LoyaltyUnit
  type: object
- description: If LoyaltyUnit is Monetary.
  name: LoyaltyCurrency
  type: string
- description: ''
  name: LoyaltyTotals
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-transaction-totals-schema.json
slug: terminal-transaction-totals
tags:
- Payments
- Financial Services
- Fintech
title: TransactionTotals
---
