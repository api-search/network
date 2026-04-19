---
description: ReportAvailableNotificationContent schema from Adyen API
layout: schema
name: ReportAvailableNotificationContent
properties_list:
- description: The code of the Account to which the report applies.
  name: accountCode
  type: string
- description: The type of Account to which the report applies.
  name: accountType
  type: string
- description: The date of the event to which the report applies.
  name: eventDate
  type: string
- description: The URL at which the report can be accessed.
  name: remoteAccessUrl
  type: string
- description: Indicates whether the event resulted in a success.
  name: success
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-report-available-notification-content-schema.json
slug: notifications-report-available-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: ReportAvailableNotificationContent
---
