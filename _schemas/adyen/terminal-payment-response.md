---
description: It conveys Information related to the Payment transaction processed by the POI System. Content of the Payment Response message.
layout: schema
name: PaymentResponse
properties_list:
- description: ''
  name: Response
  type: object
- description: ''
  name: SaleData
  type: object
- description: ''
  name: POIData
  type: object
- description: ''
  name: PaymentResult
  type: object
- description: ''
  name: LoyaltyResult
  type: array
- description: ''
  name: PaymentReceipt
  type: array
- description: ''
  name: CustomerOrder
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-payment-response-schema.json
slug: terminal-payment-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentResponse
---
