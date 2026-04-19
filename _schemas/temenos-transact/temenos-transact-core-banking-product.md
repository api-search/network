---
description: A banking product definition from the product catalog
layout: schema
name: Product
properties_list:
- description: Unique product identifier
  name: productId
  type: string
- description: Name of the product
  name: productName
  type: string
- description: Product group classification
  name: productGroup
  type: string
- description: Detailed product description
  name: description
  type: string
- description: Supported currencies
  name: currency
  type: array
- description: Interest rate conditions
  name: interestRate
  type: object
- description: Minimum balance requirement
  name: minimumBalance
  type: number
- description: Associated fees and charges
  name: fees
  type: array
- description: Product availability status
  name: status
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-product-schema.json
slug: temenos-transact-core-banking-product
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Product
---
