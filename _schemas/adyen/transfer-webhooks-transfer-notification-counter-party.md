---
description: TransferNotificationCounterParty schema from Adyen API
layout: schema
name: TransferNotificationCounterParty
properties_list:
- description: Unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id).
  name: balanceAccountId
  type: string
- description: Contains information about the bank account.
  name: bankAccount
  type: object
- description: Contains information about the merchant.
  name: merchant
  type: object
- description: Unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id).
  name: transferInstrumentId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-transfer-notification-counter-party-schema.json
slug: transfer-webhooks-transfer-notification-counter-party
tags:
- Payments
- Financial Services
- Fintech
title: TransferNotificationCounterParty
---
