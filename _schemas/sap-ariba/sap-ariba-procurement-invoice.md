---
description: An invoice document submitted by a supplier for goods or services delivered against a purchase order
layout: schema
name: Invoice
properties_list:
- description: Internal unique invoice identifier
  name: invoiceId
  type: string
- description: Supplier-assigned invoice number
  name: invoiceNumber
  type: string
- description: Date the invoice was issued
  name: invoiceDate
  type: string
- description: Type of invoice document
  name: invoiceType
  type: string
- description: Primary purchase order number this invoice relates to
  name: purchaseOrderReference
  type: string
- description: ISO 4217 currency code
  name: currency
  type: string
- description: Payment due date
  name: dueDate
  type: string
- description: Invoice line items
  name: lineItems
  type: array
- description: Header-level tax summary
  name: taxDetails
  type: array
- description: Invoice comments or notes
  name: comments
  type: string
- description: Date the invoice was approved
  name: approvalDate
  type: string
- description: Date payment was made
  name: paymentDate
  type: string
- description: Payment transaction reference number
  name: paymentReference
  type: string
- description: Timestamp when the invoice was created in the system
  name: createdDate
  type: string
- description: Timestamp of the last modification
  name: lastModifiedDate
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-invoice-schema.json
slug: sap-ariba-procurement-invoice
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: Invoice
---
