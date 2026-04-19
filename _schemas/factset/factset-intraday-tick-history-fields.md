---
description: All available fields in service. FID = Field ID Number.
layout: schema
name: fields
properties_list:
- description: 'The last bid price or last bid price in an interval. FID # 100'
  name: BID_1
  type: number
- description: 'The volume of the last bid in an interval. FID # 104'
  name: BID_VOL_1
  type: integer
- description: 'The volume of the last bid or last bid in an interval. FID # 107. Enumeration Table 7'
  name: BID_EXCH_1
  type: string
- description: 'The last ask price or last ask price in an interval. FID # 200'
  name: ASK_1
  type: number
- description: 'The volume of the last ask or last ask in an interval. FID # 204'
  name: ASK_VOL_1
  type: integer
- description: 'The exchange of the last ask or last ask in an interval. FID # 207. Enumeration Table 7.'
  name: ASK_EXCH_1
  type: string
- description: 'The last trade price or last trade price in an interval. FID # 300'
  name: LAST_1
  type: number
- description: 'The date of the last trade or last trade in an interval. FID # 301'
  name: LAST_DATE_1
  type: string
- description: 'The time of the last trade or last trade in an interval. FID # 302'
  name: LAST_TIME_1
  type: string
- description: 'The trade volume, or the sum of all trade volumes inside a bin. FID # 304'
  name: LAST_VOL_1
  type: integer
- description: 'The exchange of the last trade or last trade in an interval. FID # 307. Enumeration Table 7'
  name: LAST_EXCH_1
  type: string
- description: 'The symbol''s daily cumulative volume, or the last cumulative volume in an interval. FID # 601'
  name: CUM_VOL
  type: integer
- description: 'The daily volume weighted average price, or the last VWAP in an interval. FID # 603'
  name: VWAP
  type: number
- description: 'The first trade of an interval. FID # 710'
  name: OPEN_1
  type: number
- description: 'The highest trade price in an interval. FID # 720'
  name: HIGH_1
  type: number
- description: 'The lowest trade price in an interval. FID # 723'
  name: LOW_1
  type: number
- description: 'Trade Condition. FID # 2709'
  name: TRADE_CONDITION
  type: string
- description: 'GMT Offset in Minutes. FID # 2037'
  name: GMT_OFFSET
  type: integer
- description: 'Price Currency Code. FID # 2032'
  name: PRICE_CURRENCY
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-intraday-tick-history-fields-schema.json
slug: factset-intraday-tick-history-fields
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: fields
---
