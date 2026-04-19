---
description: Request body for updating an existing purchase order. Only provided fields will be modified.
layout: schema
name: PurchaseOrderUpdate
properties_list:
- description: Updated line items
  name: lineItems
  type: array
- description: Change request comments
  name: comments
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-purchase-order-update-schema.json
slug: sap-ariba-procurement-purchase-order-update
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: PurchaseOrderUpdate
---
