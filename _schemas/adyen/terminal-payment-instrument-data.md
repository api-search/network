---
description: Sent in the result of the payment transaction. For a card, it could also be sent in the CardAcquisition response, to be processed by the Sale System. Data related to the instrument of payment for the transaction.
layout: schema
name: PaymentInstrumentData
properties_list:
- description: ''
  name: PaymentInstrumentType
  type: object
- description: ''
  name: ProtectedCardData
  type: string
- description: ''
  name: CardData
  type: object
- description: ''
  name: CheckData
  type: object
- description: ''
  name: MobileData
  type: object
- description: ''
  name: StoredValueAccountID
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-payment-instrument-data-schema.json
slug: terminal-payment-instrument-data
tags:
- Payments
- Financial Services
- Fintech
title: PaymentInstrumentData
---
