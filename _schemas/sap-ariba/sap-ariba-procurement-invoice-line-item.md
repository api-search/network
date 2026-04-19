---
description: A line item on an invoice
layout: schema
name: InvoiceLineItem
properties_list:
- description: Line item number on the invoice
  name: lineNumber
  type: string
- description: Referenced purchase order number
  name: purchaseOrderReference
  type: string
- description: Referenced purchase order line item number
  name: poLineNumber
  type: string
- description: Item or service description
  name: description
  type: string
- description: Invoiced quantity
  name: quantity
  type: number
- description: Buyer part number
  name: buyerPartNumber
  type: string
- description: Supplier part number
  name: supplierPartNumber
  type: string
- description: Service period start date
  name: serviceStartDate
  type: string
- description: Service period end date
  name: serviceEndDate
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-invoice-line-item-schema.json
slug: sap-ariba-procurement-invoice-line-item
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: InvoiceLineItem
---
