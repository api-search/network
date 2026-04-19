---
description: A comprehensive schema representing a company entity as modeled across FactSet Fundamentals API data. Includes core identification, financial statement data, calculated ratios, consensus estimates, and segment breakdowns.
layout: schema
name: FactSet Company
properties_list:
- description: The security identifier used in the request. Accepts Market Tickers, SEDOL, ISINs, CUSIPs, or FactSet Permanent Ids.
  name: requestId
  type: string
- description: FactSet Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency.
  name: fsymId
  type:
  - string
  - 'null'
- description: The official registered name of the company.
  name: companyName
  type:
  - string
  - 'null'
- description: The market ticker symbol for the security.
  name: ticker
  type:
  - string
  - 'null'
- description: The primary stock exchange where the security is listed.
  name: exchange
  type:
  - string
  - 'null'
- description: The ISO 3166-1 alpha-2 country code for the company's primary domicile.
  name: country
  type:
  - string
  - 'null'
- description: ISO 4217 currency code for the reported financial data.
  name: currency
  type:
  - string
  - 'null'
- description: FactSet industry sector classification code.
  name: sectorCode
  type:
  - string
  - 'null'
- description: FactSet industry sub-classification code.
  name: industryCode
  type:
  - string
  - 'null'
- description: The month number (1-12) in which the company's fiscal year ends.
  name: fiscalYearEnd
  type:
  - integer
  - 'null'
- description: Standardized financial statement data organized by statement type.
  name: financialStatements
  type:
  - object
  - 'null'
- description: ''
  name: ratios
  type: object
- description: ''
  name: estimates
  type: object
- description: Business and geographic segment breakdowns.
  name: segments
  type:
  - object
  - 'null'
- description: ''
  name: metadata
  type: object
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-company-schema.json
slug: factset-company
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: FactSet Company
---
