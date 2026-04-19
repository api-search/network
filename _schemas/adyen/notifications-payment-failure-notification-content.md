---
description: PaymentFailureNotificationContent schema from Adyen API
layout: schema
name: PaymentFailureNotificationContent
properties_list:
- description: Missing or invalid fields that caused the payment error.
  name: errorFields
  type: array
- description: The error message.
  name: errorMessage
  type: object
- description: The `reference` of the capture or refund.
  name: modificationMerchantReference
  type: string
- description: The `pspReference` of the capture or refund.
  name: modificationPspReference
  type: string
- description: The `reference` of the payment.
  name: paymentMerchantReference
  type: string
- description: The `pspReference` of the payment.
  name: paymentPspReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-payment-failure-notification-content-schema.json
slug: notifications-payment-failure-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: PaymentFailureNotificationContent
---
