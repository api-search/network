---
description: ''
layout: schema
name: Invoice
properties_list:
- description: Unique document entry number
  name: DocEntry
  type: integer
- description: Document number
  name: DocNum
  type: integer
- description: Customer business partner code
  name: CardCode
  type: string
- description: Invoice date
  name: DocDate
  type: string
- description: Payment due date
  name: DocDueDate
  type: string
- description: Total invoice amount
  name: DocTotal
  type: number
- description: Invoice line items
  name: DocumentLines
  type: array
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-business-one-service-layer-invoice-schema.json
slug: sap-business-one-service-layer-invoice
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: Invoice
---
