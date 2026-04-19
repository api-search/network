---
description: PaymentData schema from Adyen API
layout: schema
name: PaymentData
properties_list:
- description: ''
  name: PaymentType
  type: object
- description: ''
  name: SplitPaymentFlag
  type: boolean
- description: ''
  name: RequestedValidityDate
  type: string
- description: ''
  name: CardAcquisitionReference
  type: object
- description: ''
  name: Instalment
  type: object
- description: ''
  name: CustomerOrder
  type: object
- description: ''
  name: PaymentInstrumentData
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-payment-data-schema.json
slug: terminal-payment-data
tags:
- Payments
- Financial Services
- Fintech
title: PaymentData
---
