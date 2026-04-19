---
description: CustomNotification schema from Adyen API
layout: schema
name: CustomNotification
properties_list:
- description: The amount of the payment that the notification is about. Set the value in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: amount
  type: object
- description: 'The event that caused the notification to be sent.Currently supported values: * **AUTHORISATION** * **CANCELLATION** * **REFUND** * **CAPTURE** * **REPORT_AVAILABLE** * **CHARGEBACK** * **REQUEST_FOR_'
  name: eventCode
  type: string
- description: 'The time of the event. Format: [ISO 8601](http://www.w3.org/TR/NOTE-datetime), YYYY-MM-DDThh:mm:ssTZD.'
  name: eventDate
  type: string
- description: Your reference for the custom test notification.
  name: merchantReference
  type: string
- description: 'The payment method for the payment that the notification is about. Possible values: * **amex** * **visa** * **mc** * **maestro** * **bcmc** * **paypal** * **sms** * **bankTransfer_NL** * **bankTransfe'
  name: paymentMethod
  type: string
- description: A descripton of what caused the notification.
  name: reason
  type: string
- description: The outcome of the event which the notification is about. Set to either **true** or **false**.
  name: success
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-custom-notification-schema.json
slug: management-custom-notification
tags:
- Payments
- Financial Services
- Fintech
title: CustomNotification
---
