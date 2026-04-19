---
description: PaymentInstrument schema from Adyen API
layout: schema
name: PaymentInstrument
properties_list:
- description: The description of the resource.
  name: description
  type: string
- description: The unique identifier of the resource.
  name: id
  type: string
- description: The reference for the resource.
  name: reference
  type: string
- description: The type of wallet the network token is associated with.
  name: tokenType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-payment-instrument-schema.json
slug: transfers-payment-instrument
tags:
- Payments
- Financial Services
- Fintech
title: PaymentInstrument
---
