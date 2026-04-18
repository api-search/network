---
description: ''
layout: schema
name: PurchaseOrderShipment
properties_list:
- description: Line location (shipment) identifier
  name: lineLocationId
  type: integer
- description: Shipment number
  name: shipmentNum
  type: integer
- description: Shipment quantity
  name: quantity
  type: number
- description: Quantity received
  name: quantityReceived
  type: number
- description: Quantity billed
  name: quantityBilled
  type: number
- description: ''
  name: needByDate
  type: string
- description: ''
  name: promisedDate
  type: string
- description: Ship-to organization identifier
  name: shipToOrganizationId
  type: integer
- description: Ship-to location identifier
  name: shipToLocationId
  type: integer
- description: Shipment close status
  name: closedCode
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-purchase-order-shipment-schema.json
slug: supply-chain-purchase-order-shipment
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: PurchaseOrderShipment
---
