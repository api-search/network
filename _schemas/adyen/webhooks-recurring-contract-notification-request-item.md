---
description: RecurringContractNotificationRequestItem schema from Adyen API
layout: schema
name: RecurringContractNotificationRequestItem
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
- description: The `pspReference` of the initial payment.
  name: originalPsp
  type: string
- description: For modifications, this field corresponds to the payment request assigned to the original payment.
  name: originalReference
  type: string
- description: The payment method used in the transaction.
  name: paymentMethod
  type: string
- description: The [token for stored payment details](https://docs.adyen.com/online-payments/tokenization/create-and-use-tokens/) to make recurring payments. This is the same as the `recurringDetailReference`.
  name: pspReference
  type: string
- description: If `success` = `false`, then this includes a short message with an explanation for the refusal.
  name: reason
  type: string
- description: 'Informs about the outcome of the event (`eventCode`) the notification is for. If `true`: the event was executed successfully. If `false`: the event was not executed successfully.'
  name: success
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-recurring-contract-notification-request-item-schema.json
slug: webhooks-recurring-contract-notification-request-item
tags:
- Payments
- Financial Services
- Fintech
title: RecurringContractNotificationRequestItem
---
