---
description: PaymentNotificationRequest-2 schema from Adyen API
layout: schema
name: PaymentNotificationRequest-2
properties_list:
- description: Contains event details.
  name: data
  type: object
- description: 'The environment from which the webhook originated. Possible values: **test**, **live**.'
  name: environment
  type: string
- description: Type of notification.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-payment-notification-request-2-schema.json
slug: notification-webhooks-payment-notification-request-2
tags:
- Payments
- Financial Services
- Fintech
title: PaymentNotificationRequest-2
---
