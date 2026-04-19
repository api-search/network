---
description: fundHolding response object
layout: schema
name: fundHolding
properties_list:
- description: Fund Identifier that was used in the request.
  name: requestId
  type: string
- description: FactSet Security Identifier of Fund. Identifies the security level id of the Fund requested (not-representing the underlying holding). Six alpha-numeric characters, excluding vowels, with an -S suffix
  name: fsymId
  type: string
- description: 'Date of the reported holding in YYYY-MM-DD format. For more details, visit [Online Assistant Page #11262](https://oa.apps.factset.com/pages/11262).'
  name: date
  type: string
- description: 'Currency code. The service will default to the funds local currency. For a list of currency ISO codes, visit [Online Assistant Page #1470](https://oa.apps.factset.com/pages/1470).'
  name: currency
  type: string
- description: Adjusted number of shares held. All positions and prices are adjusted for splits and name changes, but they are not adjusted for spinoffs or mergers. If a given company announces a split today, FactSe
  name: adjHolding
  type: number
- description: 'Adjusted market values of shares held. Market Value. All positions and prices are adjusted for splits and name changes, but they are not adjusted for spinoffs or mergers. If a given company announces '
  name: adjMarketValue
  type: number
- description: Closing weight of security in the fund for the requested asset type (percent).
  name: weightClose
  type: number
- description: 'Issue type of held security. For more details, visit [Online Assistant Page #11262](https://oa.apps.factset.com/pages/11262).'
  name: issueType
  type: string
- description: Represents the security id for the underlying holding, not the parent holding. Six alpha-numeric characters, excluding vowels, with an -S suffix (XXXXXX-S). All equity and fixed income securities that
  name: fsymSecurityId
  type: string
- description: FactSet Regional Security identifier of the security held in the fund.
  name: fsymRegionalId
  type: string
- description: Name of held security.
  name: securityName
  type: string
- description: Ticker of held security.
  name: securityTicker
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-ownership-fund-holding-schema.json
slug: factset-ownership-fund-holding
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: fundHolding
---
