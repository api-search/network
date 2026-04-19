---
description: ''
layout: schema
name: shares
properties_list:
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: Date expressed in YYYY-MM-DD format.
  name: date
  type: string
- description: Date of last split for which return has been adjusted. Use the /factset-prices/v#/splits endpoint for details on split. If not available, date will return as 0001-01-01.
  name: adjDate
  type: string
- description: '**Security-level** Common Shares Outstanding in base units. Shares sourced primarily from SEC filings. Securities in certain countries will include treasury shares. For details visit [Online Assistant'
  name: sharesSecurity
  type: number
- description: '**Company-level** Shares Outstanding aggregated across all share classes. Non-traded shares are *excluded*. In base units. For more details, visit [Online Assistant Page #16867](https://oa.apps.factse'
  name: sharesCompany
  type: number
- description: '**Company-level** Shares Outstanding aggregated across all share classes. Non-traded shares are *included* to the calculation basis by the proportion of their nominal or par value. In base units. For '
  name: sharesCompanyNontraded
  type: number
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-shares-schema.json
slug: factset-prices-shares
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: shares
---
