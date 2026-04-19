---
description: CounterpartyV3 schema from Adyen API
layout: schema
name: CounterpartyV3
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
schema_file: json-schema/accounting-notifications-counterparty-v3-schema.json
slug: accounting-notifications-counterparty-v3
tags:
- Payments
- Financial Services
- Fintech
title: CounterpartyV3
---
