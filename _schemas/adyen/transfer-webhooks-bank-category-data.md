---
description: BankCategoryData schema from Adyen API
layout: schema
name: BankCategoryData
properties_list:
- description: 'The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**. Possible values: * **regular**'
  name: priority
  type: string
- description: '**bank**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-bank-category-data-schema.json
slug: transfer-webhooks-bank-category-data
tags:
- Payments
- Financial Services
- Fintech
title: BankCategoryData
---
