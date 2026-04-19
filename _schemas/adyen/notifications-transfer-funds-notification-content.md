---
description: TransferFundsNotificationContent schema from Adyen API
layout: schema
name: TransferFundsNotificationContent
properties_list:
- description: The amount transferred.
  name: amount
  type: object
- description: The code of the Account to which funds were credited.
  name: destinationAccountCode
  type: string
- description: Invalid fields list.
  name: invalidFields
  type: array
- description: The reference provided by the merchant.
  name: merchantReference
  type: string
- description: The code of the Account from which funds were debited.
  name: sourceAccountCode
  type: string
- description: The status of the fund transfer.
  name: status
  type: object
- description: The transfer code.
  name: transferCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-transfer-funds-notification-content-schema.json
slug: notifications-transfer-funds-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: TransferFundsNotificationContent
---
