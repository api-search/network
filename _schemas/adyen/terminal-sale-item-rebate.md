---
description: To be differentiated from the award which is the amount or quantity earned on the loyalty account. The awarded amount that is attached to an item as a rebate.
layout: schema
name: SaleItemRebate
properties_list:
- description: Item identification inside a transaction (0 to n).
  name: ItemID
  type: integer
- description: Product code of item purchased with the transaction.
  name: ProductCode
  type: integer
- description: ''
  name: EanUpc
  type: integer
- description: ''
  name: UnitOfMeasure
  type: object
- description: if rebate is additional units.
  name: Quantity
  type: string
- description: if rebate on the line item amount.
  name: ItemAmount
  type: number
- description: If provided by the Acquirer.
  name: RebateLabel
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-sale-item-rebate-schema.json
slug: terminal-sale-item-rebate
tags:
- Payments
- Financial Services
- Fintech
title: SaleItemRebate
---
