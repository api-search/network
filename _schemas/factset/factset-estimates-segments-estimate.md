---
description: ''
layout: schema
name: segmentsEstimate
properties_list:
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the securitys best regional security data series per currency. For equiti
  name: fsymId
  type: string
- description: Segment selected
  name: segmentType
  type: string
- description: 'Company''s Financial statement ''metric'' that is estimated. Use the factset-estimates/v#/metrics endpoint for a complete list. For more details, visit [Online Assistant Page #15034](https://oa.apps.fact'
  name: metric
  type: string
- description: 'Company''s ''fiscal period'' for the estimate record. Periods for periodicity of ANN = 1, and SEMI = 2. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16598).'
  name: fiscalPeriod
  type: integer
- description: 'Company''s ''fiscal year'' for the estimate record. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16598)'
  name: fiscalYear
  type: integer
- description: Displays the specific label of the segment.
  name: segmentLabel
  type: string
- description: Returns the level of the segment item as either P = Parent or S = Subordinate
  name: segmentLevel
  type: string
- description: 'Company''s ''fiscal end date'' for the estimate record expressed in YYYY-MM-DD format. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16598)'
  name: fiscalEndDate
  type: string
- description: The date the estimates are as of in YYYY-MM-DD format.
  name: estimateDate
  type: string
- description: 'Currency used estimates in consensus calculations. Use ''ESTIMATE'' as input for values in Estimate Currency. For a list of currency ISO codes, visit [Online Assistant Page #1470](https://oa.apps.factse'
  name: currency
  type: string
- description: Estimate currency of the requested Security
  name: estimateCurrency
  type: string
- description: 'Mean of estimates in consensus calculation. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16114)'
  name: mean
  type: number
- description: 'Median of estimates in consensus calculation. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16114)'
  name: median
  type: number
- description: 'Standard deviation of estimates in consensus calculation. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16114)'
  name: standardDeviation
  type: number
- description: 'Highest estimate in consensus calculation. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16114).'
  name: high
  type: number
- description: 'Lowest estimate in consensus calculation. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16114)'
  name: low
  type: number
- description: 'Count or NEST of estimates in consensus calculation. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16114)'
  name: estimateCount
  type: integer
- description: 'Number of Up Revisions within the consensus for the metric and period. The default window size is 100 days For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/1611'
  name: up
  type: integer
- description: 'Number of Up Revisions within the consensus for the metric and period. The default window size is 100 days. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/161'
  name: down
  type: integer
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-estimates-segments-estimate-schema.json
slug: factset-estimates-segments-estimate
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: segmentsEstimate
---
