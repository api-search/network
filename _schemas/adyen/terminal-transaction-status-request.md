---
description: It conveys Information requested for status of the last or current Payment, Loyalty or Reversal transaction. Content of the TransactionStatus Request message.
layout: schema
name: TransactionStatusRequest
properties_list:
- description: ''
  name: MessageReference
  type: object
- description: Request to reprint the POI receipt(s).
  name: ReceiptReprintFlag
  type: boolean
- description: ''
  name: DocumentQualifier
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-transaction-status-request-schema.json
slug: terminal-transaction-status-request
tags:
- Payments
- Financial Services
- Fintech
title: TransactionStatusRequest
---
