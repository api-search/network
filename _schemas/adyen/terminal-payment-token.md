---
description: Surrogate of the PAN (Primary Account Number) of the payment card to identify the payment mean of the customer. It allows, for a merchant, to identify the customer.
layout: schema
name: PaymentToken
properties_list:
- description: ''
  name: TokenRequestedType
  type: object
- description: ''
  name: TokenValue
  type: string
- description: Expiry date and time. Limits the validity of a payment token.
  name: ExpiryDateTime
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-payment-token-schema.json
slug: terminal-payment-token
tags:
- Payments
- Financial Services
- Fintech
title: PaymentToken
---
