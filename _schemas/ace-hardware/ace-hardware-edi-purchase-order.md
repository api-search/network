---
description: An Ace Hardware EDI 850 Purchase Order representing a vendor purchase order from Ace Hardware's distribution system.
layout: schema
name: AceHardwareEdiPurchaseOrder
properties_list:
- description: Purchase order number assigned by Ace Hardware
  name: poNumber
  type: string
- description: Date the purchase order was created
  name: orderDate
  type: string
- description: Required ship-by date for the order
  name: shipByDate
  type: string
- description: Ace Hardware vendor identifier
  name: vendorId
  type: string
- description: Name of the vendor fulfilling the order
  name: vendorName
  type: string
- description: Destination distribution center or store address
  name: shipToAddress
  type: object
- description: List of products ordered
  name: lineItems
  type: array
- description: Total order value in USD
  name: totalAmount
  type: number
- description: Currency code
  name: currency
  type: string
provider_name: Ace Hardware
provider_slug: ace-hardware
schema_file: json-schema/ace-hardware-edi-purchase-order-schema.json
slug: ace-hardware-edi-purchase-order
tags:
- Retail
- Hardware
- Home Improvement
- Tools
- Paint
- Cooperative
- EDI
- Affiliate
title: AceHardwareEdiPurchaseOrder
---
