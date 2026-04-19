---
description: RevealPinRequest schema from Adyen API
layout: schema
name: RevealPinRequest
properties_list:
- description: Symmetric session key encrypted under the public key.
  name: encryptedKey
  type: string
- description: The unique identifier of the payment instrument.
  name: paymentInstrumentId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-reveal-pin-request-schema.json
slug: configuration-reveal-pin-request
tags:
- Payments
- Financial Services
- Fintech
title: RevealPinRequest
---
