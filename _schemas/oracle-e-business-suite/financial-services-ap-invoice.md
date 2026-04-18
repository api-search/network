---
description: ''
layout: schema
name: ApInvoice
properties_list:
- description: Invoice unique identifier
  name: invoiceId
  type: integer
- description: Invoice number
  name: invoiceNum
  type: string
- description: Invoice date
  name: invoiceDate
  type: string
- description: Supplier/vendor identifier
  name: vendorId
  type: integer
- description: Supplier/vendor name
  name: vendorName
  type: string
- description: Vendor site identifier
  name: vendorSiteId
  type: integer
- description: Total invoice amount
  name: invoiceAmount
  type: number
- description: Invoice currency code (ISO 4217)
  name: invoiceCurrencyCode
  type: string
- description: Payment currency code
  name: paymentCurrencyCode
  type: string
- description: Currency exchange rate
  name: exchangeRate
  type: number
- description: Exchange rate type
  name: exchangeRateType
  type: string
- description: Exchange rate date
  name: exchangeDate
  type: string
- description: Payment terms identifier
  name: termsId
  type: integer
- description: Invoice description
  name: description
  type: string
- description: Invoice type lookup code
  name: invoiceType
  type: string
- description: Invoice source
  name: source
  type: string
- description: Payment status
  name: paymentStatusFlag
  type: string
- description: Approval status
  name: approvalStatus
  type: string
- description: Amount paid
  name: amountPaid
  type: number
- description: ''
  name: lines
  type: array
- description: Operating unit identifier
  name: orgId
  type: integer
- description: ''
  name: createdBy
  type: integer
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdatedBy
  type: integer
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/financial-services-ap-invoice-schema.json
slug: financial-services-ap-invoice
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: ApInvoice
---
