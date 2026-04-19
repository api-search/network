---
description: IncomingTransferNotificationRequest schema from Adyen API
layout: schema
name: IncomingTransferNotificationRequest
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
schema_file: json-schema/notification-webhooks-incoming-transfer-notification-request-schema.json
slug: notification-webhooks-incoming-transfer-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: IncomingTransferNotificationRequest
---
