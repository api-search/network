---
description: ''
layout: schema
name: SalesOrder
properties_list:
- description: Order header identifier
  name: headerId
  type: integer
- description: Order number
  name: orderNumber
  type: integer
- description: Order date
  name: orderedDate
  type: string
- description: Order type identifier
  name: orderTypeId
  type: integer
- description: Order type name
  name: orderTypeName
  type: string
- description: Customer identifier (sold-to)
  name: soldToOrgId
  type: integer
- description: Customer name
  name: customerName
  type: string
- description: Ship-to organization identifier
  name: shipToOrgId
  type: integer
- description: Bill-to organization identifier
  name: invoiceToOrgId
  type: integer
- description: Transaction currency code (ISO 4217)
  name: transactionalCurrCode
  type: string
- description: Order flow status
  name: flowStatusCode
  type: string
- description: ''
  name: bookedFlag
  type: string
- description: Order total amount
  name: totalAmount
  type: number
- description: Salesperson identifier
  name: salesrepId
  type: integer
- description: ''
  name: lines
  type: array
- description: ''
  name: orgId
  type: integer
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-sales-order-schema.json
slug: supply-chain-sales-order
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: SalesOrder
---
