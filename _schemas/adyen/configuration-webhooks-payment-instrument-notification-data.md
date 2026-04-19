---
description: PaymentInstrumentNotificationData schema from Adyen API
layout: schema
name: PaymentInstrumentNotificationData
properties_list:
- description: The unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: Contains information about the payment instrument resource that triggered the event.
  name: paymentInstrument
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-payment-instrument-notification-data-schema.json
slug: configuration-webhooks-payment-instrument-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: PaymentInstrumentNotificationData
---
