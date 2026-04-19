---
description: 'It contains: - the identification of the stored value accounts or the stored value cards, if provided by the Sale System, and - the associated products sold by the Sale System.. Data related to the stored value card.'
layout: schema
name: StoredValueData
properties_list:
- description: If more than one provider to manage on the POI, and StoredValueAccountID absent.
  name: StoredValueProvider
  type: string
- description: ''
  name: StoredValueTransactionType
  type: object
- description: ''
  name: StoredValueAccountID
  type: object
- description: ''
  name: OriginalPOITransaction
  type: object
- description: Product code of item purchased with the transaction.
  name: ProductCode
  type: integer
- description: Standard product code of item purchased with the transaction.
  name: EanUpc
  type: integer
- description: Total amount of the item line.
  name: ItemAmount
  type: number
- description: Currency of a monetary amount.
  name: Currency
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-stored-value-data-schema.json
slug: terminal-stored-value-data
tags:
- Payments
- Financial Services
- Fintech
title: StoredValueData
---
