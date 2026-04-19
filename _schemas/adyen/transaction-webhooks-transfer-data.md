---
description: TransferData schema from Adyen API
layout: schema
name: TransferData
properties_list:
- description: The ID of the resource.
  name: id
  type: string
- description: The [`reference`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference) from the `/transfers` request. If you haven't provided any, Adyen generates a unique refere
  name: reference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transaction-webhooks-transfer-data-schema.json
slug: transaction-webhooks-transfer-data
tags:
- Payments
- Financial Services
- Fintech
title: TransferData
---
