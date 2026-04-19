---
description: AccountHolderStatusChangeNotificationContent schema from Adyen API
layout: schema
name: AccountHolderStatusChangeNotificationContent
properties_list:
- description: The code of the account holder.
  name: accountHolderCode
  type: string
- description: in case the account holder has not been updated, contains account holder fields, that did not pass the validation.
  name: invalidFields
  type: array
- description: The new status of the account holder.
  name: newStatus
  type: object
- description: The former status of the account holder.
  name: oldStatus
  type: object
- description: The reason for the status change.
  name: reason
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-account-holder-status-change-notification-content-schema.json
slug: notifications-account-holder-status-change-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderStatusChangeNotificationContent
---
