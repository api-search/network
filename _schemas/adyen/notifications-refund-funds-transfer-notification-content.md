---
description: RefundFundsTransferNotificationContent schema from Adyen API
layout: schema
name: RefundFundsTransferNotificationContent
properties_list:
- description: The amount to be refunded.
  name: amount
  type: object
- description: Invalid fields list.
  name: invalidFields
  type: array
- description: A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.
  name: merchantReference
  type: string
- description: A PSP reference of the original fund transfer.
  name: originalReference
  type: string
- description: The status of the fund transfer refund.
  name: status
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-refund-funds-transfer-notification-content-schema.json
slug: notifications-refund-funds-transfer-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: RefundFundsTransferNotificationContent
---
