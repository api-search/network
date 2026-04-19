---
description: PaymentVerificationRequest schema from Adyen API
layout: schema
name: PaymentVerificationRequest
properties_list:
- description: Encrypted and signed payment result data. You should receive this value from the Checkout SDK after the shopper completes the payment.
  name: payload
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-verification-request-schema.json
slug: checkout-payment-verification-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentVerificationRequest
---
