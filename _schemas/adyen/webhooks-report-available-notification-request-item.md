---
description: ReportAvailableNotificationRequestItem schema from Adyen API
layout: schema
name: ReportAvailableNotificationRequestItem
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
- description: Contains the file name of the report.
  name: pspReference
  type: string
- description: Contains the download URL where you can obtain a copy of the report.
  name: reason
  type: string
- description: Always `true`.
  name: success
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-report-available-notification-request-item-schema.json
slug: webhooks-report-available-notification-request-item
tags:
- Payments
- Financial Services
- Fintech
title: ReportAvailableNotificationRequestItem
---
