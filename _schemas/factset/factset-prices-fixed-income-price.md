---
description: ''
layout: schema
name: fixedIncomePrice
properties_list:
- description: Factset Security Identifier. Six alpha-numeric characters, excluding vowels, with an -S suffix (XXXXXX-S).
  name: fsymId
  type: string
- description: Ending date for the period expressed in YYYY-MM-DD format.
  name: date
  type: string
- description: Returns the security type code of fixed income instruments. * AGCY - Agency * BDNT - Bond/Note * BDWT - Bond with Warrants * BKAC - Bankers Acceptance * BLDN - Bill/Discount Note * BOND - Bond * CAP -
  name: securityType
  type: string
- description: Fixed Income Issuer Entity ID (-E).
  name: issuerEntityId
  type: string
- description: Returns the issuer type code of fixed income instruments. * AGCY - Agency * CORP - Corporate * LAUTH - Local Authority/Political Division * MUNI - Municipals * SOV - Sovereign * SUPR - Supranational *
  name: issuerType
  type: string
- description: BID PRICE. For North American issues, the value is an evaluated price, where available, else it is an exchange-traded price. Please note that distinct Bid and Ask Prices are not available for North Am
  name: priceBid
  type: number
- description: MID Price. For North American issues, the value is an evaluated price, where available, else it is an exchange-traded price. Please note that distinct Bid and Ask Prices are not available for North Am
  name: priceMid
  type: number
- description: ASK Price. For North American issues, the value is an evaluated price, where available, else it is an exchange-traded price. Please note that distinct Bid and Ask Prices are not available for North Am
  name: priceAsk
  type: number
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-fixed-income-price-schema.json
slug: factset-prices-fixed-income-price
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: fixedIncomePrice
---
