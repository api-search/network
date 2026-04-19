---
description: For each stored value card loaded or reloaded, in the StoredValue response message. Result of loading/reloading a stored value card..
layout: schema
name: StoredValueResult
properties_list:
- description: ''
  name: StoredValueTransactionType
  type: object
- description: Copy.
  name: ProductCode
  type: integer
- description: Copy.
  name: EanUpc
  type: integer
- description: Total amount of the item line.
  name: ItemAmount
  type: number
- description: Copy.
  name: Currency
  type: string
- description: ''
  name: StoredValueAccountStatus
  type: object
- description: ''
  name: HostTransactionID
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-stored-value-result-schema.json
slug: terminal-stored-value-result
tags:
- Payments
- Financial Services
- Fintech
title: StoredValueResult
---
