---
description: SweepConfigurationNotificationRequest schema from Adyen API
layout: schema
name: SweepConfigurationNotificationRequest
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
schema_file: json-schema/notification-webhooks-sweep-configuration-notification-request-schema.json
slug: notification-webhooks-sweep-configuration-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: SweepConfigurationNotificationRequest
---
