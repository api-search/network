---
description: Convertible Details for a Fixed Income security.
layout: schema
name: convertibleHistory
properties_list:
- description: Security identifier used in the request.
  name: requestId
  type: string
- description: FactSet Permanent Security Identifier.
  name: fsymId
  type: string
- description: Convertible Effective Date
  name: convEffDate
  type: string
- description: Convertibles Price
  name: convPrice
  type: number
- description: Convertibles Ratio
  name: convRatio
  type: number
- description: Convertibles Underlying FactSet Permanent Identifier
  name: convUlyFsymId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-terms-and-conditions-convertible-history-schema.json
slug: factset-terms-and-conditions-convertible-history
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: convertibleHistory
---
