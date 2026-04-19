---
description: AchNotificationOfChangeNotificationRequest schema from Adyen API
layout: schema
name: AchNotificationOfChangeNotificationRequest
properties_list:
- description: Timestamp for when the webhook was created.
  name: createdAt
  type: string
- description: Contains details of the update.
  name: data
  type: object
- description: 'The environment from which the webhook originated. Possible values: **test**, **live**.'
  name: environment
  type: string
- description: Type of notification.
  name: type
  type: string
- description: The version of this webhook type.
  name: version
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-ach-notification-of-change-notification-request-schema.json
slug: webhooks-ach-notification-of-change-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: AchNotificationOfChangeNotificationRequest
---
