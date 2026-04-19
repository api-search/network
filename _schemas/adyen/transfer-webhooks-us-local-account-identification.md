---
description: USLocalAccountIdentification schema from Adyen API
layout: schema
name: USLocalAccountIdentification
properties_list:
- description: The bank account number, without separators or whitespace.
  name: accountNumber
  type: string
- description: 'The bank account type. Possible values: **checking** or **savings**. Defaults to **checking**.'
  name: accountType
  type: string
- description: The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace.
  name: routingNumber
  type: string
- description: '**usLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-us-local-account-identification-schema.json
slug: transfer-webhooks-us-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: USLocalAccountIdentification
---
