---
description: ''
layout: schema
name: Order
properties_list:
- description: Unique document entry number
  name: DocEntry
  type: integer
- description: Document number
  name: DocNum
  type: integer
- description: Business partner code
  name: CardCode
  type: string
- description: Document date
  name: DocDate
  type: string
- description: Document due date
  name: DocDueDate
  type: string
- description: Total document amount
  name: DocTotal
  type: number
- description: Document currency
  name: DocCurrency
  type: string
- description: Order line items
  name: DocumentLines
  type: array
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-business-one-service-layer-order-schema.json
slug: sap-business-one-service-layer-order
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: Order
---
