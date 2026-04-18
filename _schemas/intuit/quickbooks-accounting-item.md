---
description: An Item represents a product or service that a company buys, sells, or re-sells. Items are used in line items on invoices, sales receipts, bills, and other transactions.
layout: schema
name: Item
properties_list:
- description: Unique identifier for the item
  name: Id
  type: string
- description: Version number for optimistic locking
  name: SyncToken
  type: string
- description: Name of the item. Must be unique within the same type.
  name: Name
  type: string
- description: Description of the item used in sales transactions
  name: Description
  type: string
- description: Description of the item used in purchase transactions
  name: PurchaseDesc
  type: string
- description: Whether the item is currently active
  name: Active
  type: boolean
- description: Fully qualified name of the item
  name: FullyQualifiedName
  type: string
- description: Whether sales of this item are taxable
  name: Taxable
  type: boolean
- description: Whether the sales tax is included in the item amount
  name: SalesTaxIncluded
  type: boolean
- description: Sales price for this item
  name: UnitPrice
  type: number
- description: Classification of the item
  name: Type
  type: string
- description: Purchase cost of the item
  name: PurchaseCost
  type: number
- description: Current quantity on hand (inventory items only)
  name: QtyOnHand
  type: number
- description: Date of opening balance for inventory items
  name: InvStartDate
  type: string
- description: Whether quantity on hand is tracked
  name: TrackQtyOnHand
  type: boolean
- description: Stock keeping unit identifier
  name: Sku
  type: string
- description: Whether this is a sub-item
  name: SubItem
  type: boolean
- description: Depth level in the item hierarchy
  name: Level
  type: integer
- description: ''
  name: AbatementRate
  type: number
- description: ''
  name: ReverseChargeRate
  type: number
- description: ''
  name: domain
  type: string
- description: ''
  name: sparse
  type: boolean
provider_name: Intuit
provider_slug: intuit
schema_file: json-schema/quickbooks-accounting-item-schema.json
slug: quickbooks-accounting-item
tags:
- Accounting
- Custom Fields
- Financial
- Financial Services
- Invoicing
- Payments
- Payroll
- Project Management
- Sales Tax
- Small Business
- Tax
- Tax Preparation
- Taxes
- Time Tracking
title: Item
---
