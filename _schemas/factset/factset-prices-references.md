---
description: ''
layout: schema
name: references
properties_list:
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: The name of the security.
  name: name
  type: string
- description: 'Security Type Description. For more details, visit [Online Assistant Page #10149](https://oa.apps.factset.com/pages/10149).'
  name: secType
  type: string
- description: 'General Security Type Code. For more details regarding what the code represents, visit [Online Assistant Page #10149](https://oa.apps.factset.com/pages/10149).'
  name: secTypeCode
  type: string
- description: 'Detailed Security Type Code. For more details regarding what the code represents, visit [Online Assistant Page #10149](https://oa.apps.factset.com/pages/10149).'
  name: secTypeCodeDet
  type: string
- description: 'Currency ISO code. For more details, visit [Online Assistant Page #1470](https://oa.apps.factset.com/pages/1470).'
  name: currency
  type: string
- description: 'Country Name. Returns the country where the security is *traded* from the North American Pricing database. Therefore, for securities covered by the North American Pricing database, will return either '
  name: country
  type: string
- description: 'Primary Exchange Name. For more details, visit [Online Assistant Page #16610](https://oa.apps.factset.com/pages/16610).'
  name: primaryExchange
  type: string
- description: Returns the location of the exchange where the company's stock is traded.
  name: exchangeCountry
  type: string
- description: 'The Local Index ID for the company''s home country benchmark. For more details, visit [Online Assistant Page #10698](https://oa.apps.factset.com/pages/10698).'
  name: localIndex
  type: string
- description: 'The Next Trading Holiday. For more details regarding Global Trading Holiday Schedules, visit [Online Assistant Page #10397](https://oa.apps.factset.com/pages/10397).'
  name: nextTradingHolidayDate
  type: string
- description: The Security's Date of First Trade. It will return the first date that the FactSet Pricing database began to cover the security and it may not coincide with the actual IPO date. Pricing information fo
  name: firstDate
  type: string
- description: Date of Last Trade. It will return the last date that the FactSet Pricing database as a record for this security listing.
  name: lastDate
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-references-schema.json
slug: factset-prices-references
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: references
---
