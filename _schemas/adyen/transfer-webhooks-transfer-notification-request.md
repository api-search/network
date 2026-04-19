---
description: TransferNotificationRequest schema from Adyen API
layout: schema
name: TransferNotificationRequest
properties_list:
- description: Contains details about the event.
  name: data
  type: object
- description: 'The environment from which the webhook originated. Possible values: **test**, **live**.'
  name: environment
  type: string
- description: The type of webhook.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-transfer-notification-request-schema.json
slug: transfer-webhooks-transfer-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: TransferNotificationRequest
---
