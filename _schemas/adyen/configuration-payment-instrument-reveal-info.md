---
description: PaymentInstrumentRevealInfo schema from Adyen API
layout: schema
name: PaymentInstrumentRevealInfo
properties_list:
- description: The CVC2 value of the card.
  name: cvc
  type: string
- description: The expiration date of the card.
  name: expiration
  type: object
- description: The primary account number (PAN) of the card.
  name: pan
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-payment-instrument-reveal-info-schema.json
slug: configuration-payment-instrument-reveal-info
tags:
- Payments
- Financial Services
- Fintech
title: PaymentInstrumentRevealInfo
---
