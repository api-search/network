---
description: SweepConfigurationNotificationData schema from Adyen API
layout: schema
name: SweepConfigurationNotificationData
properties_list:
- description: The unique identifier of the balance account for which the sweep was configured.
  name: accountId
  type: string
- description: Unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: Contains information about the sweep resource that triggered the event.
  name: sweep
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-sweep-configuration-notification-data-schema.json
slug: notification-webhooks-sweep-configuration-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: SweepConfigurationNotificationData
---
