---
description: PaymentNotificationRequest schema from Adyen API
layout: schema
name: PaymentNotificationRequest
properties_list:
- description: Contains event details.
  name: data
  type: object
- description: 'The environment from which the webhook originated. Possible values: **test**, **live**.'
  name: environment
  type: string
- description: Type of webhook.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-payment-notification-request-schema.json
slug: configuration-webhooks-payment-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentNotificationRequest
---
