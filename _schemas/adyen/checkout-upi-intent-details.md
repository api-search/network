---
description: UpiIntentDetails schema from Adyen API
layout: schema
name: UpiIntentDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: The `shopperNotificationReference` returned in the response when you requested to notify the shopper. Used for recurring payment only.
  name: shopperNotificationReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**upi_intent**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-upi-intent-details-schema.json
slug: checkout-upi-intent-details
tags:
- Payments
- Financial Services
- Fintech
title: UpiIntentDetails
---
