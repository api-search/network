---
description: ExpireNotificationRequestItem schema from Adyen API
layout: schema
name: ExpireNotificationRequestItem
properties_list:
- description: A generic container for extra fields.
  name: additionalData
  type: object
- description: The amount that was originally authorised.
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
- description: Adyen's 16-character unique reference associated with the transaction or request. This value is globally unique. Use it when communicating with us about this request.
  name: pspReference
  type: string
- description: If `success` = `false`, then this includes a short message with an explanation for the refusal.
  name: reason
  type: string
- description: Always `true`.
  name: success
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-expire-notification-request-item-schema.json
slug: webhooks-expire-notification-request-item
tags:
- Payments
- Financial Services
- Fintech
title: ExpireNotificationRequestItem
---
