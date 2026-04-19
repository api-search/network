---
description: If the payment receipts are printed by the Sale system and the POI or the Sale does not implement the Print exchange (Basic profile). Customer or Merchant payment receipt.
layout: schema
name: PaymentReceipt
properties_list:
- description: ''
  name: DocumentQualifier
  type: object
- description: Type of the print integrated to other prints.
  name: IntegratedPrintFlag
  type: boolean
- description: Indicate that the cardholder payment receipt requires a physical signature by the Customer.
  name: RequiredSignatureFlag
  type: boolean
- description: ''
  name: OutputContent
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-payment-receipt-schema.json
slug: terminal-payment-receipt
tags:
- Payments
- Financial Services
- Fintech
title: PaymentReceipt
---
