---
description: CheckoutQrCodeAction schema from Adyen API
layout: schema
name: CheckoutQrCodeAction
properties_list:
- description: Expiry time of the QR code.
  name: expiresAt
  type: string
- description: Encoded payment data.
  name: paymentData
  type: string
- description: Specifies the payment method.
  name: paymentMethodType
  type: string
- description: The contents of the QR code as a UTF8 string.
  name: qrCodeData
  type: string
- description: '**qrCode**'
  name: type
  type: string
- description: Specifies the URL to redirect to.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-checkout-qr-code-action-schema.json
slug: checkout-checkout-qr-code-action
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutQrCodeAction
---
