---
description: Request sent to terminal to initiate payment. It conveys Information related to the Payment transaction to process. Content of the Payment Request message.
layout: schema
name: PaymentRequest
properties_list:
- description: ''
  name: SaleData
  type: object
- description: ''
  name: PaymentTransaction
  type: object
- description: ''
  name: PaymentData
  type: object
- description: ''
  name: LoyaltyData
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-payment-request-schema.json
slug: terminal-payment-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentRequest
---
