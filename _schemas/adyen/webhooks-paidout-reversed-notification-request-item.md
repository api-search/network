---
description: PaidoutReversedNotificationRequestItem schema from Adyen API
layout: schema
name: PaidoutReversedNotificationRequestItem
properties_list:
- description: A generic container for extra fields.
  name: additionalData
  type: object
- description: The payment amount. For HTTP POST notifications, currency and value are returned as URL parameters.
  name: amount
  type: object
- description: The type of event the notification item is for.
  name: eventCode
  type: string
- description: 'The time when the event was generated. Format: ISO 8601; yyyy-MM-DDThh:mm:ssTZD'
  name: eventDate
  type: string
- description: The merchant account identifier used in the transaction the notification item is for.
  name: merchantAccountCode
  type: string
- description: Your reference to uniquely identify the payment.
  name: merchantReference
  type: string
- description: For modifications, this field corresponds to the payment request assigned to the original payment.
  name: originalReference
  type: string
- description: The payment method used in the transaction.
  name: paymentMethod
  type: string
- description: The PSP reference for the Capture's PSP reference.
  name: pspReference
  type: string
- description: Contains the bank statement description if present, else it contains `PaidOutReversed`.
  name: reason
  type: string
- description: 'Informs about the outcome of the event (`eventCode`) the notification is for. If `true`: the event was executed successfully. If `false`: the event was not executed successfully.'
  name: success
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-paidout-reversed-notification-request-item-schema.json
slug: webhooks-paidout-reversed-notification-request-item
tags:
- Payments
- Financial Services
- Fintech
title: PaidoutReversedNotificationRequestItem
---
