---
description: NotificationModificationData schema from Adyen API
layout: schema
name: NotificationModificationData
properties_list:
- description: The amount of the modification converted to the balance account's currency, in case the original transaction currency is different. For example, if a part of an authorised amount was cancelled, the va
  name: amount
  type: object
- description: 'The type of modification. Possible values: **Authorised**, **Cancelled**, **Captured**, **Error**, **Expired**, **OutgoingTransfer**, **PendingIncomingTransfer**, **PendingRefund**, **IncomingTransfer'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-notification-modification-data-schema.json
slug: notification-webhooks-notification-modification-data
tags:
- Payments
- Financial Services
- Fintech
title: NotificationModificationData
---
