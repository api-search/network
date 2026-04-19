---
description: PaymentMethodIssuer schema from Adyen API
layout: schema
name: PaymentMethodIssuer
properties_list:
- description: A boolean value indicating whether this issuer is unavailable. Can be `true` whenever the issuer is offline.
  name: disabled
  type: boolean
- description: The unique identifier of this issuer, to submit in requests to /payments.
  name: id
  type: string
- description: A localized name of the issuer.
  name: name
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-method-issuer-schema.json
slug: checkout-payment-method-issuer
tags:
- Payments
- Financial Services
- Fintech
title: PaymentMethodIssuer
---
