---
description: Request body for creating a new invoice
layout: schema
name: InvoiceCreate
properties_list:
- description: Supplier-assigned invoice number
  name: invoiceNumber
  type: string
- description: Invoice issue date
  name: invoiceDate
  type: string
- description: ''
  name: invoiceType
  type: string
- description: Purchase order number
  name: purchaseOrderReference
  type: string
- description: ''
  name: currency
  type: string
- description: ''
  name: lineItems
  type: array
- description: ''
  name: comments
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-invoice-create-schema.json
slug: sap-ariba-procurement-invoice-create
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: InvoiceCreate
---
