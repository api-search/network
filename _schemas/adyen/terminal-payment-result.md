---
description: PaymentResult schema from Adyen API
layout: schema
name: PaymentResult
properties_list:
- description: ''
  name: PaymentType
  type: object
- description: ''
  name: PaymentInstrumentData
  type: object
- description: ''
  name: AmountsResp
  type: object
- description: ''
  name: Instalment
  type: object
- description: ''
  name: CurrencyConversion
  type: array
- description: ''
  name: MerchantOverrideFlag
  type: boolean
- description: ''
  name: CapturedSignature
  type: object
- description: ''
  name: ProtectedSignature
  type: string
- description: ''
  name: CustomerLanguage
  type: string
- description: ''
  name: OnlineFlag
  type: boolean
- description: ''
  name: AuthenticationMethod
  type: object
- description: ''
  name: ValidityDate
  type: string
- description: ''
  name: PaymentAcquirerData
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-payment-result-schema.json
slug: terminal-payment-result
tags:
- Payments
- Financial Services
- Fintech
title: PaymentResult
---
