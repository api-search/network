---
description: DetailBalance schema from Adyen API
layout: schema
name: DetailBalance
properties_list:
- description: The list of balances held by the account.
  name: balance
  type: array
- description: The list of on hold balances held by the account.
  name: onHoldBalance
  type: array
- description: The list of pending balances held by the account.
  name: pendingBalance
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-detail-balance-schema.json
slug: funds-detail-balance
tags:
- Payments
- Financial Services
- Fintech
title: DetailBalance
---
