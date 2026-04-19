---
description: ''
layout: schema
name: summaries
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: FactSet Entity Identifier. Six alpha-numeric characters, excluding vowels, with a -E suffix (XXXXXX-E), resolved from the requestId of the Fund requested.
  name: fsymEntityId
  type: string
- description: FactSet Regional Identifier. Six alpha-numeric characters, excluding vowels, with a -R suffix (XXXXXX-R), resolved from the requestId of the Fund requested.
  name: fsymRegionalId
  type: string
- description: FactSet Ticker-Region for the requested fund.
  name: fsymTickerRegion
  type: string
- description: The FactSet Ultimate Parent Entity Identifer, with a -E suffix (XXXXXX-E).
  name: fsymUltimateParentId
  type: string
- description: The requested Id sent as input.
  name: requestId
  type: string
- description: Binary flag to indicate whether the fund is currently active, where 1 is active and 0 is inactive.
  name: activeFlag
  type: integer
- description: Binary indicator of whether the fund is actively managed, where 1 is active and 0 is inactive.
  name: activelyManagedFlag
  type: integer
- description: The Funds Brand Name in proper format.
  name: brand
  type: string
- description: Returns the fund's country of domicile in ISO2 format. Only available for Mutual Funds.
  name: countryDomicile
  type: string
- description: The fund's currency.
  name: currency
  type: string
- description: The Fund's Investment Strategy short description.
  name: descInfo
  type: string
- description: The fund of fund's id if applicable. Will provide plain Fund of Funds text.
  name: fundOfFundsId
  type: string
- description: The fund's inception date in YYYY-MM-DD format.
  name: inceptionDate
  type: string
- description: The fund's investment strategy long description. Use `descInfo` if needing short description.
  name: insight
  type: string
- description: The Issuer Identifier.
  name: issuerId
  type: string
- description: The Issuer Name in proper format.
  name: issuerName
  type: string
- description: The legal structure of the fund, e.g. Open-Ended Fund, close-ended fund
  name: legalStructure
  type: string
- description: The leverage factor of the fund.
  name: leverageFactor
  type: number
- description: Indicates whether the fund is leveraged, inverse, or neither in proper format.
  name: leverageInverse
  type: string
- description: The Fund security's name in proper format.
  name: name
  type: string
- description: The NAV currency for the specified share class.
  name: navCurrency
  type: string
- description: The Fund's objective long description.
  name: objective
  type: string
- description: 'The fund''s first available date for prices (NAV) in YYYY-MM-DD format. This can be used to fetch the first available price from FactSet. *NOTE: This is not the inception date of fund.*'
  name: priceFirstDate
  type: string
- description: The fund's most recent available date for prices (NAV) in YYYY-MM-DD format.
  name: priceRecentDate
  type: string
- description: The Funds Share class type name in proper format.
  name: shrClass
  type: string
- description: Returns a binary indicator of whether the specified share class is currently active, where 1 is active and 0 is inactive.
  name: shrClassActiveFlag
  type: integer
- description: Returns a binary indicator of whether the specified share class is actively managed, where 1 is active and 0 is inactive.
  name: shrClsActivelyManagedFlag
  type: integer
- description: The currency for the specified share class.
  name: shrClsCurrency
  type: string
- description: The specified share class's inception date in YYYY-MM-DD format.
  name: shrClsInceptDate
  type: string
- description: The specified share class name for the fund in proper format.
  name: shrClsName
  type: string
- description: The Share class Termination Date in YYYY-MM-DD format. If still active, value will be null.
  name: shrClsTermDate
  type: string
- description: The Termination Date in YYYY-MM-DD format. If still active, value will be null.
  name: terminationDate
  type: string
- description: The Type of Fund, e.g. Mutual Fund, Unit Investment Trust
  name: type
  type: string
- description: The URL of the Fund.
  name: webSite
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-funds-summaries-schema.json
slug: factset-funds-summaries
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: summaries
---
