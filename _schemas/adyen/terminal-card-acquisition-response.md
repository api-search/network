---
description: It conveys Information related to the payment and loyalty cards read and processed by the POI System and entered by the Customer. Content of the Card Acquisition Response message.
layout: schema
name: CardAcquisitionResponse
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
- description: Data related to the POI System.
  name: CustomerLanguage
  type: string
- description: ''
  name: PaymentBrand
  type: array
- description: ''
  name: PaymentInstrumentData
  type: object
- description: ''
  name: LoyaltyAccount
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-card-acquisition-response-schema.json
slug: terminal-card-acquisition-response
tags:
- Payments
- Financial Services
- Fintech
title: CardAcquisitionResponse
---
