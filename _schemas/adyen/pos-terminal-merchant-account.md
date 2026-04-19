---
description: MerchantAccount schema from Adyen API
layout: schema
name: MerchantAccount
properties_list:
- description: List of terminals assigned to this merchant account as in-store terminals. This means that the terminal is ready to be boarded, or is already boarded.
  name: inStoreTerminals
  type: array
- description: List of terminals assigned to the inventory of this merchant account.
  name: inventoryTerminals
  type: array
- description: The merchant account.
  name: merchantAccount
  type: string
- description: Array of stores under this merchant account.
  name: stores
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/pos-terminal-merchant-account-schema.json
slug: pos-terminal-merchant-account
tags:
- Payments
- Financial Services
- Fintech
title: MerchantAccount
---
