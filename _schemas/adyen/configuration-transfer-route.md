---
description: TransferRoute schema from Adyen API
layout: schema
name: TransferRoute
properties_list:
- description: 'The type of transfer. Possible values: - **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account'
  name: category
  type: string
- description: The two-character ISO-3166-1 alpha-2 country code of the counterparty. For example, **US** or **NL**.
  name: country
  type: string
- description: The three-character ISO currency code of transfer. For example, **USD** or **EUR**.
  name: currency
  type: string
- description: 'The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Possible values: * **regular**: For normal, low-value transactions. * **fast**:'
  name: priority
  type: string
- description: A set of rules defined by clearing houses and banking partners. Your transfer request must adhere to these rules to ensure successful initiation of transfer. Based on the priority, one or more require
  name: requirements
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-transfer-route-schema.json
slug: configuration-transfer-route
tags:
- Payments
- Financial Services
- Fintech
title: TransferRoute
---
