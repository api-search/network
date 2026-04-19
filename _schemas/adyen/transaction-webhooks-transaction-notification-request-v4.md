---
description: TransactionNotificationRequestV4 schema from Adyen API
layout: schema
name: TransactionNotificationRequestV4
properties_list:
- description: Contains details about the event.
  name: data
  type: object
- description: 'The environment from which the webhook originated. Possible values: **test**, **live**.'
  name: environment
  type: string
- description: Type of the webhook.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transaction-webhooks-transaction-notification-request-v4-schema.json
slug: transaction-webhooks-transaction-notification-request-v4
tags:
- Payments
- Financial Services
- Fintech
title: TransactionNotificationRequestV4
---
