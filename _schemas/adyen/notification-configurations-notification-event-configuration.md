---
description: NotificationEventConfiguration schema from Adyen API
layout: schema
name: NotificationEventConfiguration
properties_list:
- description: 'The type of event. Possible values: **ACCOUNT_CLOSED**, **ACCOUNT_CREATED**, **ACCOUNT_FUNDS_BELOW_THRESHOLD**, **ACCOUNT_HOLDER_CREATED**, **ACCOUNT_HOLDER_LIMIT_REACHED**, **ACCOUNT_HOLDER_PAYOUT**,'
  name: eventType
  type: string
- description: 'Indicates whether the specified `eventType` is sent to your webhook endpoint. Possible values: * **INCLUDE**: Send the specified `eventType`. * **EXCLUDE**: Send all event types except the specified `'
  name: includeMode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-configurations-notification-event-configuration-schema.json
slug: notification-configurations-notification-event-configuration
tags:
- Payments
- Financial Services
- Fintech
title: NotificationEventConfiguration
---
