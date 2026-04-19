---
description: Counterparty schema from Adyen API
layout: schema
name: Counterparty
properties_list:
- description: Contains information about the bank account.
  name: bankAccount
  type: object
- description: Unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id).
  name: transferInstrumentId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-counterparty-schema.json
slug: configuration-counterparty
tags:
- Payments
- Financial Services
- Fintech
title: Counterparty
---
