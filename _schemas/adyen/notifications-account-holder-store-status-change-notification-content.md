---
description: AccountHolderStoreStatusChangeNotificationContent schema from Adyen API
layout: schema
name: AccountHolderStoreStatusChangeNotificationContent
properties_list:
- description: The code of the account holder.
  name: accountHolderCode
  type: string
- description: In case the store status has not been updated, contains fields that did not pass the validation.
  name: invalidFields
  type: array
- description: The new status of the account holder.
  name: newStatus
  type: string
- description: The former status of the account holder.
  name: oldStatus
  type: string
- description: The reason for the status change.
  name: reason
  type: string
- description: Alphanumeric identifier of the store.
  name: store
  type: string
- description: Store store reference.
  name: storeReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-account-holder-store-status-change-notification-content-schema.json
slug: notifications-account-holder-store-status-change-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderStoreStatusChangeNotificationContent
---
