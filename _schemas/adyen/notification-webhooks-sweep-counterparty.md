---
description: SweepCounterparty schema from Adyen API
layout: schema
name: SweepCounterparty
properties_list:
- description: The unique identifier of the destination or source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id). You can only use this for periodic
  name: balanceAccountId
  type: string
- description: The merchant account that will be the source of funds, if you are processing payments with Adyen. You can only use this with sweeps of `type` **pull** and `schedule.type` **balance**.
  name: merchantAccount
  type: string
- description: The unique identifier of the destination or source [transfer instrument](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/transferInstruments__resParam_id). You can also use this in c
  name: transferInstrumentId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-sweep-counterparty-schema.json
slug: notification-webhooks-sweep-counterparty
tags:
- Payments
- Financial Services
- Fintech
title: SweepCounterparty
---
