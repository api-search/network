---
description: BalanceAccountNotificationRequest schema from Adyen API
layout: schema
name: BalanceAccountNotificationRequest
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
schema_file: json-schema/notification-webhooks-balance-account-notification-request-schema.json
slug: notification-webhooks-balance-account-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: BalanceAccountNotificationRequest
---
