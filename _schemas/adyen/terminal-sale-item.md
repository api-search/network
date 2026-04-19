---
description: In loyalty or value added payment card transaction, the items of the sale are entering in the processing of the transaction. Sale items of a transaction.
layout: schema
name: SaleItem
properties_list:
- description: Item identification inside a transaction (0 to n).
  name: ItemID
  type: integer
- description: Product code of item purchased with the transaction.
  name: ProductCode
  type: integer
- description: If data sent, POI has to store it and send it if the host protocol allows it.
  name: EanUpc
  type: integer
- description: ''
  name: UnitOfMeasure
  type: object
- description: If data sent, POI has to store it and send it if the host protocol allows it.
  name: Quantity
  type: string
- description: if Quantity present.
  name: UnitPrice
  type: number
- description: Total amount of the item line.
  name: ItemAmount
  type: number
- description: If data sent, POI has to store it and send it if the host protocol allows it.
  name: TaxCode
  type: integer
- description: If data sent, POI has to store it and send it if the host protocol allows it.
  name: SaleChannel
  type: integer
- description: ''
  name: ProductLabel
  type: string
- description: If data sent, POI has to store it and send it if the host protocol allows it.
  name: AdditionalProductInfo
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-sale-item-schema.json
slug: terminal-sale-item
tags:
- Payments
- Financial Services
- Fintech
title: SaleItem
---
