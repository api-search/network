---
description: AuthorisationNotificationRequestItem schema from Adyen API
layout: schema
name: AuthorisationNotificationRequestItem
properties_list:
- description: This object is a generic container that can hold extra fields.
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
- description: The operations indicate the supported follow-up actions concerning the payment. > This is an **experimental field**. Do not base your code on this field. Not all specific cases are covered yet. It's p
  name: operations
  type: array
- description: The payment method used in the transaction.
  name: paymentMethod
  type: string
- description: Adyen's 16-character unique reference associated with the transaction or request. This value is globally unique. Use it when communicating with us about this request.
  name: pspReference
  type: string
- description: 'If `success` = `true` and `paymentMethod` = `visa`, `mc`, or `amex` then this field contains the following details: Authorisation code, last 4 digits of the card, card expiry date. In case of failure,'
  name: reason
  type: string
- description: 'If `true`: The payment request was successful. If `false`: The payment request failed. Check the `reason` field for failure information.'
  name: success
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-authorisation-notification-request-item-schema.json
slug: webhooks-authorisation-notification-request-item
tags:
- Payments
- Financial Services
- Fintech
title: AuthorisationNotificationRequestItem
---
