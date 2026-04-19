---
description: SweepCounterparty schema from Adyen API
layout: schema
name: SweepCounterparty
properties_list:
- description: The unique identifier of the destination or source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id). You can only use this for periodic
  name: balanceAccountId
  type: string
- description: The merchant account that will be the source of funds. You can only use this parameter with sweeps of `type` **pull** and `schedule.type` **balance**, and if you are processing payments with Adyen.
  name: merchantAccount
  type: string
- description: The unique identifier of the destination or source [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id) depending on the sweep `type`
  name: transferInstrumentId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-sweep-counterparty-schema.json
slug: configuration-webhooks-sweep-counterparty
tags:
- Payments
- Financial Services
- Fintech
title: SweepCounterparty
---
