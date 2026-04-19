---
description: A goods receipt or service confirmation recorded against a purchase order
layout: schema
name: Receipt
properties_list:
- description: Unique receipt identifier
  name: receiptId
  type: string
- description: Reference to the purchase order
  name: purchaseOrderId
  type: string
- description: Date goods were received or services confirmed
  name: receiptDate
  type: string
- description: Type of receipt
  name: receiptType
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: lineItems
  type: array
- description: ''
  name: createdDate
  type: string
- description: User who created the receipt
  name: createdBy
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-receipt-schema.json
slug: sap-ariba-procurement-receipt
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: Receipt
---
