---
description: Convertible Details for a Fixed Income security.
layout: schema
name: convertibleDetails
properties_list:
- description: Security identifier used in the request.
  name: requestId
  type: string
- description: FactSet Permanent Security Identifier.
  name: fsymId
  type: string
- description: Convertible Currency
  name: convCurr
  type: string
- description: Convertible Effective Date
  name: convEffDate
  type: string
- description: Convertible End Date
  name: convEndDate
  type: string
- description: Convertible Frequency
  name: convFrequency
  type: string
- description: Convertible Type Id
  name: convId
  type: integer
- description: Convertible Identification
  name: convIdentification
  type: string
- description: Convertible Notice Max
  name: convNoticeDaysMax
  type: integer
- description: Convertible Notice Min
  name: convNoticeDaysMin
  type: integer
- description: Convertible Payment Form
  name: convPayForm
  type: string
- description: Convertible Payment Form Detail
  name: convPayFormDet
  type: string
- description: Convertible Payment Form Election
  name: convPayFormElect
  type: string
- description: Convertible Premium Change Control
  name: convPremChgControl
  type: number
- description: Convertible Price Method
  name: convPriceMethod
  type: string
- description: Convertibles Ratio
  name: convRatio
  type: number
- description: Convertible Ratio Form Description
  name: convRatioDesc
  type: string
- description: Convertible Type
  name: convType
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-terms-and-conditions-convertible-details-schema.json
slug: factset-terms-and-conditions-convertible-details
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: convertibleDetails
---
