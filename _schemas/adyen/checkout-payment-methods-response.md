---
description: PaymentMethodsResponse schema from Adyen API
layout: schema
name: PaymentMethodsResponse
properties_list:
- description: Detailed list of payment methods required to generate payment forms.
  name: paymentMethods
  type: array
- description: List of all stored payment methods.
  name: storedPaymentMethods
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-methods-response-schema.json
slug: checkout-payment-methods-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentMethodsResponse
---
