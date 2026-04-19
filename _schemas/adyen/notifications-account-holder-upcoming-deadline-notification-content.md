---
description: AccountHolderUpcomingDeadlineNotificationContent schema from Adyen API
layout: schema
name: AccountHolderUpcomingDeadlineNotificationContent
properties_list:
- description: The code of the account holder whom the event refers to.
  name: accountHolderCode
  type: string
- description: The event name that will be trigger if no action is taken.
  name: event
  type: string
- description: The execution date scheduled for the event.
  name: executionDate
  type: string
- description: The reason that leads to scheduling of the event.
  name: reason
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-account-holder-upcoming-deadline-notification-content-schema.json
slug: notifications-account-holder-upcoming-deadline-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderUpcomingDeadlineNotificationContent
---
