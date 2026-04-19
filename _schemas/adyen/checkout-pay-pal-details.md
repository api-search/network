---
description: PayPalDetails schema from Adyen API
layout: schema
name: PayPalDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The unique ID associated with the order.
  name: orderID
  type: string
- description: IMMEDIATE_PAYMENT_REQUIRED or UNRESTRICTED
  name: payeePreferred
  type: string
- description: The unique ID associated with the payer.
  name: payerID
  type: string
- description: PAYPAL or PAYPAL_CREDIT
  name: payerSelected
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: The type of flow to initiate.
  name: subtype
  type: string
- description: '**paypal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-pay-pal-details-schema.json
slug: checkout-pay-pal-details
tags:
- Payments
- Financial Services
- Fintech
title: PayPalDetails
---
