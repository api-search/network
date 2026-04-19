---
description: It conveys Information related to the reversal processed by the POI System. Content of the Reversal Response message.
layout: schema
name: ReversalResponse
properties_list:
- description: ''
  name: Response
  type: object
- description: ''
  name: POIData
  type: object
- description: ''
  name: OriginalPOITransaction
  type: object
- description: Copy.
  name: ReversedAmount
  type: number
- description: ''
  name: CustomerOrder
  type: array
- description: ''
  name: PaymentReceipt
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-reversal-response-schema.json
slug: terminal-reversal-response
tags:
- Payments
- Financial Services
- Fintech
title: ReversalResponse
---
