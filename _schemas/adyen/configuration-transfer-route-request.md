---
description: TransferRouteRequest schema from Adyen API
layout: schema
name: TransferRouteRequest
properties_list:
- description: The unique identifier of the source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id). Required if `counterparty` is **transferInstrumen
  name: balanceAccountId
  type: string
- description: The unique identifier assigned to the balance platform associated with the account holder.
  name: balancePlatform
  type: string
- description: 'The type of transfer. Possible values: - **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account'
  name: category
  type: string
- description: The recipient of the funds transfer. A bank account or a transfer instrument.
  name: counterparty
  type: object
- description: The two-character ISO-3166-1 alpha-2 country code of the counterparty. For example, **US** or **NL**. > Either `counterparty` or `country` field must be provided in a transfer route request.
  name: country
  type: string
- description: The three-character ISO currency code of transfer. For example, **USD** or **EUR**.
  name: currency
  type: string
- description: 'The list of priorities for the bank transfer. Priorities set the speed at which the transfer is sent and the fees that you have to pay. Multiple values can be provided. Possible values: * **regular**:'
  name: priorities
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-transfer-route-request-schema.json
slug: configuration-transfer-route-request
tags:
- Payments
- Financial Services
- Fintech
title: TransferRouteRequest
---
