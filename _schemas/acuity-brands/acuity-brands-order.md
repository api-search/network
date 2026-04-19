---
description: An Acuity Brands order with status and shipment information
layout: schema
name: Order
properties_list:
- description: Acuity Brands order number
  name: orderId
  type: string
- description: Distributor purchase order number
  name: purchaseOrderNumber
  type: string
- description: ''
  name: status
  type: string
- description: Date order was placed
  name: orderDate
  type: string
- description: Estimated ship date
  name: estimatedShipDate
  type: string
- description: Actual ship date
  name: actualShipDate
  type: string
- description: Order line items
  name: lineItems
  type: array
- description: Total order amount
  name: totalAmount
  type: number
- description: ''
  name: shipToAddress
  type: object
provider_name: acuity-brands
provider_slug: acuity-brands
schema_file: json-schema/acuity-brands-order-schema.json
slug: acuity-brands-order
tags: []
title: Order
---
