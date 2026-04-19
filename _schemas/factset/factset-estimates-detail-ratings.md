---
description: ''
layout: schema
name: detailRatings
properties_list:
- description: ''
  name: fsymId
  type: string
- description: 'Date of estimate expressed in YYYY-MM-DD format. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16598)'
  name: estimateDate
  type: string
- description: The FactSet Entity Identifier for the analyst making the estimate.
  name: analystId
  type: string
- description: The name of the analyst making the estimate.
  name: analystName
  type: string
- description: The FactSet Entity Identifier for the broker making the estimate.
  name: brokerId
  type: string
- description: The name of the broker making the estimate.
  name: brokerName
  type: string
- description: 'A textual representation of the analysts rating. Broker recommendations are divided into five main broad categories- **Buy, Overweight, Hold, Underweight, and Sell**.<p>Additional recommendations may '
  name: ratingsNoteText
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: Date and time when the data is available at the source.
  name: inputDateTime
  type: string
- description: The date at which a broker provided an estimate that is a revision.
  name: lastModifiedDate
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-estimates-detail-ratings-schema.json
slug: factset-estimates-detail-ratings
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: detailRatings
---
