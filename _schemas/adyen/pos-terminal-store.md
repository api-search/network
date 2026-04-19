---
description: Store schema from Adyen API
layout: schema
name: Store
properties_list:
- description: The address of the store.
  name: address
  type: object
- description: The description of the store.
  name: description
  type: string
- description: The list of terminals assigned to the store.
  name: inStoreTerminals
  type: array
- description: The code of the merchant account.
  name: merchantAccountCode
  type: string
- description: 'The status of the store: - `PreActive`: the store has been created, but not yet activated. - `Active`: the store has been activated. This means you can process payments for this store. - `Inactive`: t'
  name: status
  type: string
- description: The code of the store.
  name: store
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/pos-terminal-store-schema.json
slug: pos-terminal-store
tags:
- Payments
- Financial Services
- Fintech
title: Store
---
