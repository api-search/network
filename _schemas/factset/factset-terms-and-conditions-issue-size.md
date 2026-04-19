---
description: Issue Size Data Items for a Fixed Income security.
layout: schema
name: issueSize
properties_list:
- description: Security identifier used in the request.
  name: requestId
  type: string
- description: FactSet Permanent Security Identifier.
  name: fsymId
  type: string
- description: Amount Outstanding Effective Date (out_amt_eff_date)
  name: outAmtEffDate
  type: string
- description: Amount Outstanding Currency
  name: outAmtCurrency
  type: string
- description: Amount Outstanding
  name: outAmt
  type: number
- description: Amount Outstanding Action Amount
  name: outAmtChange
  type: number
- description: Price - Amount Outstanding Action
  name: outAmtChangePrice
  type: number
- description: Amount Outstanding Action Type
  name: outAmtChangeType
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-terms-and-conditions-issue-size-schema.json
slug: factset-terms-and-conditions-issue-size
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: issueSize
---
