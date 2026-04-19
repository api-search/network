---
description: Currency definition with exchange rate information
layout: schema
name: Currency
properties_list:
- description: ISO 4217 currency code
  name: currencyCode
  type: string
- description: Full currency name
  name: currencyName
  type: string
- description: ISO 4217 numeric code
  name: numericCode
  type: string
- description: Number of decimal places
  name: decimalPlaces
  type: integer
- description: Current buy exchange rate
  name: buyRate
  type: number
- description: Current sell exchange rate
  name: sellRate
  type: number
- description: Mid-market exchange rate
  name: midRate
  type: number
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-currency-schema.json
slug: temenos-transact-core-banking-currency
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Currency
---
