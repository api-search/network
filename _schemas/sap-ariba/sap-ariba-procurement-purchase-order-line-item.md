---
description: A line item within a purchase order representing a specific good or service being procured
layout: schema
name: PurchaseOrderLineItem
properties_list:
- description: Line item number within the purchase order. Unique within the order.
  name: numberOnPO
  type: string
- description: Description of the item or service being purchased
  name: description
  type: string
- description: Quantity to purchase
  name: quantity
  type: number
- description: Buyer-assigned part or material number
  name: buyerPartNumber
  type: string
- description: Supplier-assigned part or catalog number
  name: supplierPartNumber
  type: string
- description: Manufacturer part identifier
  name: manufacturerPartId
  type: string
- description: Name of the manufacturer
  name: manufacturerName
  type: string
- description: Item category code distinguishing material, service, or other item types
  name: itemCategory
  type: string
- description: Account assignment category for the line item expenditure
  name: accountCategory
  type: string
- description: Requested delivery date for the line item (ISO 8601 YYYY-MM-DD)
  name: needByDate
  type: string
- description: Split accounting assignments for distributing costs across multiple cost objects
  name: accountings
  type: array
- description: Receiving type value indicating how receipts should be processed for this line item
  name: receivingType
  type: integer
- description: Tax code per evaluated receipt settlement agreements
  name: taxCode
  type: string
- description: Line number of the corresponding item in the originating requisition
  name: itemOnRequisition
  type: string
- description: Service period start date (for service line items)
  name: serviceStartDate
  type: string
- description: Service period end date (for service line items)
  name: serviceEndDate
  type: string
- description: Additional comments or notes on the line item
  name: comments
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-purchase-order-line-item-schema.json
slug: sap-ariba-procurement-purchase-order-line-item
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: PurchaseOrderLineItem
---
