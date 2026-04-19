---
description: UpiCollectDetails schema from Adyen API
layout: schema
name: UpiCollectDetails
properties_list:
- description: The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper.
  name: billingSequenceNumber
  type: string
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
- description: '**upi_collect**'
  name: type
  type: string
- description: The virtual payment address for UPI.
  name: virtualPaymentAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-upi-collect-details-schema.json
slug: checkout-upi-collect-details
tags:
- Payments
- Financial Services
- Fintech
title: UpiCollectDetails
---
