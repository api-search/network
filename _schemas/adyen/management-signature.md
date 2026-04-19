---
description: Signature schema from Adyen API
layout: schema
name: Signature
properties_list:
- description: If `skipSignature` is false, indicates whether the shopper should provide a signature on the display (**true**) or on the merchant receipt (**false**).
  name: askSignatureOnScreen
  type: boolean
- description: Name that identifies the terminal.
  name: deviceName
  type: string
- description: Slogan shown on the start screen of the device.
  name: deviceSlogan
  type: string
- description: Skip asking for a signature. This is possible because all global card schemes (American Express, Diners, Discover, JCB, MasterCard, VISA, and UnionPay) regard a signature as optional.
  name: skipSignature
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-signature-schema.json
slug: management-signature
tags:
- Payments
- Financial Services
- Fintech
title: Signature
---
