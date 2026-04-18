---
description: ''
layout: schema
name: Supplier
properties_list:
- description: Vendor identifier
  name: vendorId
  type: integer
- description: Vendor name
  name: vendorName
  type: string
- description: Vendor number
  name: segment1
  type: string
- description: Vendor type lookup code
  name: vendorType
  type: string
- description: Tax payer identification number
  name: taxPayerId
  type: string
- description: Standard industry classification
  name: standardIndustryClass
  type: string
- description: Default payment currency
  name: paymentCurrencyCode
  type: string
- description: Default payment method
  name: paymentMethodCode
  type: string
- description: Default payment terms identifier
  name: termsId
  type: integer
- description: Whether the vendor is active
  name: enabled
  type: boolean
- description: ''
  name: startDateActive
  type: string
- description: ''
  name: endDateActive
  type: string
- description: ''
  name: sites
  type: array
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-supplier-schema.json
slug: supply-chain-supplier
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Supplier
---
