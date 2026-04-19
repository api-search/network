---
description: CompensateNegativeBalanceNotificationRecord schema from Adyen API
layout: schema
name: CompensateNegativeBalanceNotificationRecord
properties_list:
- description: The code of the account whose negative balance has been compensated.
  name: accountCode
  type: string
- description: The amount compensated.
  name: amount
  type: object
- description: The date on which the compensation took place.
  name: transferDate
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-compensate-negative-balance-notification-record-schema.json
slug: notifications-compensate-negative-balance-notification-record
tags:
- Payments
- Financial Services
- Fintech
title: CompensateNegativeBalanceNotificationRecord
---
