---
description: DirectDebitInitiatedNotificationContent schema from Adyen API
layout: schema
name: DirectDebitInitiatedNotificationContent
properties_list:
- description: The code of the account.
  name: accountCode
  type: string
- description: The amount to be debited from the funding account.
  name: amount
  type: object
- description: The date of the debit initiation.
  name: debitInitiationDate
  type: object
- description: Invalid fields list.
  name: invalidFields
  type: array
- description: The code of the merchant account.
  name: merchantAccountCode
  type: string
- description: The split data for the debit request.
  name: splits
  type: array
- description: Direct debit status.
  name: status
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-direct-debit-initiated-notification-content-schema.json
slug: notifications-direct-debit-initiated-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: DirectDebitInitiatedNotificationContent
---
