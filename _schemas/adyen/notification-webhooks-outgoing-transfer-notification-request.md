---
description: OutgoingTransferNotificationRequest schema from Adyen API
layout: schema
name: OutgoingTransferNotificationRequest
properties_list:
- description: Contains details about the event.
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
schema_file: json-schema/notification-webhooks-outgoing-transfer-notification-request-schema.json
slug: notification-webhooks-outgoing-transfer-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: OutgoingTransferNotificationRequest
---
