---
description: CompensateNegativeBalanceNotification schema from Adyen API
layout: schema
name: CompensateNegativeBalanceNotification
properties_list:
- description: Details of the negative balance compensation.
  name: content
  type: object
- description: Error information of failed request. No value provided here if no error occurred on processing.
  name: error
  type: object
- description: The date and time when an event has been completed.
  name: eventDate
  type: string
- description: The event type of the notification.
  name: eventType
  type: string
- description: The user or process that has triggered the notification.
  name: executingUserKey
  type: string
- description: Indicates whether the notification originated from the live environment or the test environment. If true, the notification originated from the live environment. If false, the notification originated f
  name: live
  type: boolean
- description: The PSP reference of the request from which the notification originates.
  name: pspReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-compensate-negative-balance-notification-schema.json
slug: notifications-compensate-negative-balance-notification
tags:
- Payments
- Financial Services
- Fintech
title: CompensateNegativeBalanceNotification
---
