---
description: AccountHolderUpcomingDeadlineNotification schema from Adyen API
layout: schema
name: AccountHolderUpcomingDeadlineNotification
properties_list:
- description: The details of the upcoming event.
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
schema_file: json-schema/notifications-account-holder-upcoming-deadline-notification-schema.json
slug: notifications-account-holder-upcoming-deadline-notification
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderUpcomingDeadlineNotification
---
