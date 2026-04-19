---
description: MerchantUpdatedNotificationRequest schema from Adyen API
layout: schema
name: MerchantUpdatedNotificationRequest
properties_list:
- description: Timestamp for when the webhook was created.
  name: createdAt
  type: string
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
schema_file: json-schema/management-webhooks-merchant-updated-notification-request-schema.json
slug: management-webhooks-merchant-updated-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: MerchantUpdatedNotificationRequest
---
