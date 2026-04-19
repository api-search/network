---
description: ''
layout: schema
name: Dividend
properties_list:
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: FactSet identifier that uniquely identifies the Event.
  name: eventId
  type: string
- description: Corporate Actions Event type code.
  name: eventTypeCode
  type: string
- description: Corporate Actions Event type description.
  name: eventTypeDesc
  type: string
- description: 'Dividend Type Code. For code descriptions, visit [Online Assistant Page #8764] (https://oa.apps.factset.com/pages/8764).'
  name: divTypeCode
  type: string
- description: Date Event was announced in YYYY-MM-DD format.
  name: announcementDate
  type: string
- description: Date of Record for distribution in YYYY-MM-DD format.
  name: recordDate
  type: string
- description: Date of Payment for distribution in YYYY-MM-DD format.
  name: payDate
  type: string
- description: Effective Date or Ex-Date of distribution in YYYY-MM-DD format.
  name: effectiveDate
  type: string
- description: 'Currency ISO code. For more details, visit [Online Assistant Page #1470](https://oa.apps.factset.com/pages/1470).'
  name: currency
  type: string
- description: 'Net/Gross Marker Code. For details describing Net vs. Gross dividends, visit [Online Assistant Page #11512](https://oa.apps.factset.com/pages/11512).'
  name: amtDefNetGrossIndicator
  type: string
- description: Default Amount - Trading Currency, Split Adjusted
  name: amtDefTradingAdj
  type: number
- description: Default Amount - Trading Currency, Unadjusted
  name: amtDefTradingUnadj
  type: number
- description: Gross Amount - Trading Currency, Split Adjusted
  name: amtGrossTradingAdj
  type: number
- description: Gross Amount - Trading Currency, Unadjusted
  name: amtGrossTradingUnadj
  type: number
- description: Net Amount - Trading Currency, Split Adjusted
  name: amtNetTradingAdj
  type: number
- description: Net Amount - Trading Currency, Unadjusted
  name: amtNetTradingUnadj
  type: number
- description: Currency code for declared dividend.
  name: declaredCurrency
  type: string
- description: Default Amount - Declared Currency, Split Adjusted
  name: amtDefDecAdj
  type: number
- description: Default Amount - Declared Currency, Unadjusted
  name: amtDefDecUnadj
  type: number
- description: Gross Amount - Declared Currency, Split Adjusted
  name: amtGrossDecAdj
  type: number
- description: Gross Amount - Declared Currency, Unadjusted
  name: amtGrossDecUnadj
  type: number
- description: Net Amount - Declared Currency, Split Adjusted
  name: amtNetDecAdj
  type: number
- description: Net Amount - Declared Currency, Unadjusted
  name: amtNetDecUnadj
  type: number
- description: Dividend Status Flag - 1=Yes, 0=No
  name: dividendStatus
  type: integer
- description: Dividend active Flag - 1=Yes, 0=No
  name: dividendActiveFlag
  type: integer
- description: Special Dividend Flag - 1=Yes, 0=No
  name: dividendsSpecFlag
  type: integer
- description: Default Frank - Trading Currency, Split Adjusted
  name: frankDefTradingAdj
  type: number
- description: Default Frank - Trading Currency, Unadjusted
  name: frankDefTradingUnadj
  type: number
- description: Default Frank - Declared Currency, Split Adjusted
  name: frankDefDecAdj
  type: number
- description: Default Frank - Declared Currency, Unadjusted
  name: frankDefDecUnadj
  type: number
- description: Default Amount - Declared Currency, Unadjusted
  name: frankPct
  type: number
- description: Tax Rate for on gross dividend for net dividend.
  name: taxRate
  type: number
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-global-prices-dividend-schema.json
slug: factset-global-prices-dividend
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: Dividend
---
