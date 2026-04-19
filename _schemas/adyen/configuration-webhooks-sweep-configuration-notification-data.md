---
description: SweepConfigurationNotificationData schema from Adyen API
layout: schema
name: SweepConfigurationNotificationData
properties_list:
- description: The unique identifier of the balance account for which the sweep was configured.
  name: accountId
  type: string
- description: The unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: Contains information about the sweep resource that triggered the event.
  name: sweep
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-sweep-configuration-notification-data-schema.json
slug: configuration-webhooks-sweep-configuration-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: SweepConfigurationNotificationData
---
