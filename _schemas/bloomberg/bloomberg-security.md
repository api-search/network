---
description: A financial security as represented in the Bloomberg BLPAPI data universe. Bloomberg tracks over 35 million instruments across equities, fixed income, derivatives, commodities, currencies, and alternative assets through services including //blp/refdata, //blp/mktdata, and //blp/mktbar. Securities are identified using Bloomberg tickers, FIGI, ISIN, CUSIP, SEDOL, and Bloomberg Unique Identifiers (BBUID). Based on bloomberg.github.io/blpapi-docs.
layout: schema
name: Bloomberg Security
properties_list:
- description: Bloomberg Unique Identifier (BBUID) - the primary internal Bloomberg security identifier.
  name: bbuid
  type: string
- description: Financial Instrument Global Identifier (FIGI) assigned by Bloomberg as the open, standard global identifier.
  name: figi
  type: string
- description: Bloomberg ticker symbol including asset class suffix used in BLPAPI requests (e.g., AAPL US Equity, CL1 Comdty, SPX Index, JPY Curncy).
  name: ticker
  type: string
- description: International Securities Identification Number (ISIN) for cross-border security identification.
  name: isin
  type: string
- description: Committee on Uniform Securities Identification Procedures (CUSIP) identifier, used primarily for US and Canadian securities.
  name: cusip
  type: string
- description: Stock Exchange Daily Official List (SEDOL) identifier. BLPAPI supports symbology lookup via /sedol1/ prefix (e.g., /sedol1/2840215).
  name: sedol
  type: string
- description: 'Full legal name of the security or issuer (BLPAPI field: Security_Name or NAME).'
  name: name
  type: string
- description: 'Abbreviated name of the security as displayed on Bloomberg Terminal (BLPAPI field: SHORT_NAME).'
  name: shortName
  type: string
- description: 'Extended company or instrument description (BLPAPI field: LONG_COMP_NAME).'
  name: longCompanyName
  type: string
- description: 'Bloomberg security description providing concise instrument details (BLPAPI field: SECURITY_DES).'
  name: securityDescription
  type: string
- description: Bloomberg security type classification determining which market data fields and services are available.
  name: securityType
  type: string
- description: 'Primary exchange where the security is listed, using Bloomberg exchange codes (BLPAPI field: EXCH_CODE).'
  name: exchange
  type: string
- description: 'ISO 4217 three-letter currency code for the security''s primary trading currency (BLPAPI field: CRNCY).'
  name: currency
  type: string
- description: 'ISO 3166-1 alpha-2 country code of the security''s country of domicile (BLPAPI field: COUNTRY_ISO).'
  name: country
  type: string
- description: 'GICS sector classification for the security (BLPAPI field: GICS_SECTOR_NAME).'
  name: sector
  type: string
- description: 'GICS industry group classification (BLPAPI field: GICS_INDUSTRY_GROUP_NAME).'
  name: industryGroup
  type: string
- description: 'Bloomberg Industry Classification Standard (BICS) industry code (BLPAPI field: INDUSTRY_GROUP).'
  name: industry
  type: string
- description: 'GICS sub-industry classification (BLPAPI field: GICS_SUB_INDUSTRY_NAME).'
  name: subIndustry
  type: string
- description: 'Market capitalization in the security''s primary trading currency (BLPAPI field: MARKET_CAP or CUR_MKT_CAP).'
  name: marketCap
  type: number
- description: 'Total number of shares currently outstanding (BLPAPI field: EQY_SH_OUT).'
  name: sharesOutstanding
  type: number
- description: ''
  name: pricing
  type: object
- description: ''
  name: fundamentals
  type: object
- description: ''
  name: referenceData
  type: object
- description: ''
  name: esgScores
  type: object
- description: 'Credit ratings from major rating agencies as reported via Bloomberg (BLPAPI fields: RTG_MOODY, RTG_SP, RTG_FITCH).'
  name: creditRatings
  type: array
- description: ''
  name: dividends
  type: object
- description: Whether the security is currently active and trading on its primary exchange.
  name: active
  type: boolean
provider_name: Bloomberg
provider_slug: bloomberg
schema_file: json-schema/bloomberg-security-schema.json
slug: bloomberg-security
tags:
- Analytics
- Business Intelligence
- Data License
- Enterprise
- Execution Management
- Financial Services
- Market Data
- News
- Quantitative Analysis
- Trading
- Transaction Cost Analysis
title: Bloomberg Security
---
