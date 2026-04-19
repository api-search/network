---
description: Allows acquisition of the card data by the Sale System before the Payment, CardAcquisition or BalanceInquiry request to the POI. It could also be sent in the CardAcquisition response, to be processed by the Sale System. Information related to the payment card used for the transaction.
layout: schema
name: CardData
properties_list:
- description: If card PAN is readable .
  name: PaymentBrand
  type: string
- description: ''
  name: MaskedPan
  type: string
- description: ''
  name: PaymentAccountRef
  type: string
- description: ''
  name: EntryMode
  type: object
- description: If available in the card.
  name: CardCountryCode
  type: integer
- description: SensitiveCardData protected by CMS EnvelopedData.
  name: ProtectedCardData
  type: string
- description: ''
  name: SensitiveCardData
  type: object
- description: ''
  name: AllowedProductCode
  type: array
- description: ''
  name: AllowedProduct
  type: array
- description: ''
  name: PaymentToken
  type: object
- description: ''
  name: CustomerOrder
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-card-data-schema.json
slug: terminal-card-data
tags:
- Payments
- Financial Services
- Fintech
title: CardData
---
