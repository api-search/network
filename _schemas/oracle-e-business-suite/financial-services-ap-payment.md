---
description: ''
layout: schema
name: ApPayment
properties_list:
- description: Payment check identifier
  name: checkId
  type: integer
- description: Check number
  name: checkNumber
  type: integer
- description: Payment amount
  name: amount
  type: number
- description: Payment currency code
  name: currencyCode
  type: string
- description: Check date
  name: checkDate
  type: string
- description: Vendor identifier
  name: vendorId
  type: integer
- description: Vendor name
  name: vendorName
  type: string
- description: Bank account identifier
  name: bankAccountId
  type: integer
- description: Payment method
  name: paymentMethodCode
  type: string
- description: Payment status
  name: status
  type: string
- description: ''
  name: orgId
  type: integer
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/financial-services-ap-payment-schema.json
slug: financial-services-ap-payment
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: ApPayment
---
