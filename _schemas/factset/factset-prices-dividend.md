---
description: ''
layout: schema
name: dividend
properties_list:
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: Ex-Date of the dividend expressed in YYYY-MM-DD format.
  name: divsExDate
  type: string
- description: Date of last split for which prices and volume have been adjusted.
  name: adjDate
  type: string
- description: 'Currency ISO code. For more details, visit [Online Assistant Page #1470](https://oa.apps.factset.com/pages/1470).'
  name: currency
  type: string
- description: Amount of the dividend paid.
  name: divsPaid
  type: number
- description: Date the dividend was recorded expressed in YYYY-MM-DD format.
  name: divsRecDate
  type: string
- description: Date the dividend will be paid expressed in YYYY-MM-DD format.
  name: divsPayDate
  type: string
- description: 'Dividend type code. For code descriptions, visit [Online Assistant Page #8764](https://oa.apps.factset.com/pages/8764).'
  name: divsTypeC
  type: integer
- description: 'Description of dividend type. For type descriptions, visit [Online Assistant Page #8764](https://oa.apps.factset.com/pages/8764).'
  name: divsTypeD
  type: string
- description: 'Tax Marker Code. For code descriptions, visit [Online Assistant Page #15265](https://oa.apps.factset.com/pages/15265).'
  name: divsTaxC
  type: string
- description: 'Description of Tax Marker. For type descriptions, visit [Online Assistant Page #15265](https://oa.apps.factset.com/pages/15265).'
  name: divsTaxD
  type: string
- description: 'Net/Gross Marker Code. For details describing Net vs. Gross dividends, visit [Online Assistant Page #11512](https://oa.apps.factset.com/pages/11512).'
  name: divsNGFlag
  type: string
- description: 'Net/Gross equivalent (opposite of dividend paid). For details describing Net vs. Gross dividends, visit [Online Assistant Page #11512](https://oa.apps.factset.com/pages/11512).'
  name: divsNGEquiv
  type: number
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-dividend-schema.json
slug: factset-prices-dividend
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: dividend
---
