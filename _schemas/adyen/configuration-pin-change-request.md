---
description: PinChangeRequest schema from Adyen API
layout: schema
name: PinChangeRequest
properties_list:
- description: Symmetric session key encrypted under the public key.
  name: encryptedKey
  type: string
- description: The encrypted PIN block
  name: encryptedPinBlock
  type: string
- description: The unique identifier of the payment instrument.
  name: paymentInstrumentId
  type: string
- description: The token which is used to construct the pinblock.
  name: token
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-pin-change-request-schema.json
slug: configuration-pin-change-request
tags:
- Payments
- Financial Services
- Fintech
title: PinChangeRequest
---
