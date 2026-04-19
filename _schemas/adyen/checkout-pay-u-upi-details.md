---
description: PayUUpiDetails schema from Adyen API
layout: schema
name: PayUUpiDetails
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
- description: '**payu_IN_upi**'
  name: type
  type: string
- description: The virtual payment address for UPI.
  name: virtualPaymentAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-pay-u-upi-details-schema.json
slug: checkout-pay-u-upi-details
tags:
- Payments
- Financial Services
- Fintech
title: PayUUpiDetails
---
