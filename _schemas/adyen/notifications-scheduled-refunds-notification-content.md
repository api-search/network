---
description: ScheduledRefundsNotificationContent schema from Adyen API
layout: schema
name: ScheduledRefundsNotificationContent
properties_list:
- description: The code of the account.
  name: accountCode
  type: string
- description: The code of the Account Holder.
  name: accountHolderCode
  type: string
- description: Invalid fields list.
  name: invalidFields
  type: array
- description: The most recent payout (after which all transactions were scheduled to be refunded).
  name: lastPayout
  type: object
- description: A list of the refunds that have been scheduled and their results.
  name: refundResults
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-scheduled-refunds-notification-content-schema.json
slug: notifications-scheduled-refunds-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: ScheduledRefundsNotificationContent
---
