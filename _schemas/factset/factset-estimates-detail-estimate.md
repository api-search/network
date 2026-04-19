---
description: ''
layout: schema
name: detailEstimate
properties_list:
- description: ''
  name: fsymId
  type: string
- description: 'Company''s Financial statement ''metric'' that is estimated. Use the factset-estimates/v#/metrics endpoint for a complete list. For more details, visit [Online Assistant Page #15034](https://oa.apps.fact'
  name: metric
  type: string
- description: Company's 'periodicity' for the estimate record, reflecting Annual, Quarterly, or Semi-Annual report periods.
  name: periodicity
  type: string
- description: Company's 'fiscal year' for the estimate record
  name: fiscalYear
  type: integer
- description: Company's 'fiscal period' for the estimate record. 'Periodicity' defines context for period.
  name: fiscalPeriod
  type: integer
- description: Company's 'fiscal end date' for the estimate record expressed in YYYY-MM-DD format
  name: fiscalEndDate
  type: string
- description: '''Fiscal period'' based on relationship to ''estimate date''. This is not applicable for fixed-consensus endpoint. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/'
  name: relativePeriod
  type: integer
- description: 'Currency code for adjusting the data. Use ''ESTIMATE'' as input value for the values in Estimate Currency. For a list of currency ISO codes, visit [Online Assistant Page #1470](https://oa.apps.factset.c'
  name: currency
  type: string
- description: 'Date of estimate expressed in YYYY-MM-DD format. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16598)'
  name: estimateDate
  type: string
- description: The value of the estimate.
  name: estimateValue
  type: number
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
- description: The date at which a broker provided an estimate that is a revision.
  name: lastModifiedDate
  type: string
- description: 'Date the previous estimate was made expressed in YYYY-MM-DD format. For more details, visit [Online Assistant Page #16598](https://oa.apps.factset.com/pages/16598)'
  name: prevEstimateDate
  type: string
- description: The value of the previous estimate.
  name: prevEstimateValue
  type: number
- description: Section of the estimate.Returns the details of brokers inlcuded and excluded in the consensus
  name: section
  type: string
- description: Status code of the estimate.
  name: statusCode
  type: integer
- description: Status description of the estimate.
  name: statusText
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: Date and time when the data is available at the source.
  name: inputDateTime
  type: string
- description: The currency that the company trades in.
  name: securityCurrency
  type: string
- description: The currency in which estimates are made by broker.
  name: brokerEstimateCurrency
  type: string
- description: Estimate currency of the requested Security
  name: estimateCurrency
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-estimates-detail-estimate-schema.json
slug: factset-estimates-detail-estimate
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: detailEstimate
---
