---
description: ''
layout: schema
name: ArInvoice
properties_list:
- description: Customer transaction identifier
  name: customerTrxId
  type: integer
- description: Transaction number
  name: trxNumber
  type: string
- description: Transaction date
  name: trxDate
  type: string
- description: Customer identifier
  name: customerId
  type: integer
- description: Customer name
  name: customerName
  type: string
- description: Bill-to site use identifier
  name: billToSiteUseId
  type: integer
- description: Ship-to site use identifier
  name: shipToSiteUseId
  type: integer
- description: Invoice currency (ISO 4217)
  name: invoiceCurrencyCode
  type: string
- description: Transaction type
  name: trxType
  type: string
- description: Transaction amount
  name: amount
  type: number
- description: Remaining amount due
  name: amountDue
  type: number
- description: Transaction status
  name: status
  type: string
- description: Payment terms identifier
  name: termsId
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
schema_file: json-schema/financial-services-ar-invoice-schema.json
slug: financial-services-ar-invoice
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: ArInvoice
---
