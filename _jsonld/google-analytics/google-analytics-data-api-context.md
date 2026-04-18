---
class_count: 10
classes:
- AudienceExport
- DateRange
- Dimension
- FilterExpression
- Metric
- OrderBy
- Pivot
- Row
- RunReportRequest
- RunReportResponse
context_file: json-ld/google-analytics-data-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/json-ld/google-analytics-data-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Google Analytics Data Api from Google Analytics.
layout: jsonld
name: Google Analytics Data Api Context
namespaces:
- prefix: ga
  uri: https://developers.google.com/analytics/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: accumulate
  type: boolean
- container: set
  name: activeMetricRestrictions
  type: string
- container: ''
  name: andGroup
  type: string
- container: ''
  name: audience
  type: string
- container: ''
  name: audienceDisplayName
  type: string
- container: ''
  name: beginCreatingTime
  type: dateTime
- container: ''
  name: betweenFilter
  type: string
- container: ''
  name: caseSensitive
  type: boolean
- container: ''
  name: cohortReportSettings
  type: reference
- container: ''
  name: cohortSpec
  type: reference
- container: set
  name: cohorts
  type: string
- container: ''
  name: cohortsRange
  type: reference
- container: ''
  name: concatenate
  type: reference
- container: ''
  name: concurrentRequests
  type: reference
- container: ''
  name: consumed
  type: integer
- container: ''
  name: creationQuotaTokensCharged
  type: integer
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: dataLossFromOtherRow
  type: boolean
- container: set
  name: dateRanges
  type: reference
- container: ''
  name: delimiter
  type: string
- container: ''
  name: desc
  type: boolean
- container: ''
  name: dimension
  type: reference
- container: ''
  name: dimensionExpression
  type: reference
- container: ''
  name: dimensionFilter
  type: reference
- container: set
  name: dimensionHeaders
  type: reference
- container: ''
  name: dimensionName
  type: string
- container: set
  name: dimensionNames
  type: string
- container: set
  name: dimensionValues
  type: reference
- container: set
  name: dimensions
  type: reference
- container: ''
  name: emptyReason
  type: string
- container: ''
  name: endDate
  type: string
- container: ''
  name: endOffset
  type: integer
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: expression
  type: string
- container: set
  name: expressions
  type: string
- container: ''
  name: fieldName
  type: string
- container: set
  name: fieldNames
  type: string
- container: ''
  name: filter
  type: string
- container: ''
  name: fromValue
  type: string
- container: ''
  name: granularity
  type: string
- container: ''
  name: inListFilter
  type: string
- container: ''
  name: invisible
  type: boolean
- container: ''
  name: keepEmptyRows
  type: boolean
- container: ''
  name: kind
  type: string
- container: ''
  name: limit
  type: string
- container: ''
  name: lowerCase
  type: reference
- container: ''
  name: matchType
  type: string
- container: set
  name: maximums
  type: reference
- container: ''
  name: metadata
  type: reference
- container: ''
  name: metric
  type: reference
- container: set
  name: metricAggregations
  type: string
- container: ''
  name: metricFilter
  type: reference
- container: set
  name: metricHeaders
  type: reference
- container: ''
  name: metricName
  type: string
- container: set
  name: metricValues
  type: reference
- container: set
  name: metrics
  type: reference
- container: set
  name: minimums
  type: reference
- container: ''
  name: name
  type: string
- container: ''
  name: notExpression
  type: string
- container: ''
  name: numericFilter
  type: string
- container: ''
  name: offset
  type: string
- container: ''
  name: operation
  type: string
- container: ''
  name: orGroup
  type: reference
- container: set
  name: orderBys
  type: reference
- container: ''
  name: orderType
  type: string
- container: ''
  name: percentageCompleted
  type: double
- container: ''
  name: pivot
  type: reference
- container: set
  name: pivotSelections
  type: string
- container: ''
  name: potentiallyThresholdedRequestsPerHour
  type: reference
- container: ''
  name: property
  type: string
- container: ''
  name: propertyQuota
  type: reference
- container: ''
  name: remaining
  type: integer
- container: ''
  name: returnPropertyQuota
  type: boolean
- container: ''
  name: rowCount
  type: integer
- container: set
  name: rows
  type: reference
- container: set
  name: samplingMetadatas
  type: string
- container: ''
  name: schemaRestrictionResponse
  type: reference
- container: ''
  name: serverErrorsPerProjectPerHour
  type: reference
- container: ''
  name: startDate
  type: string
- container: ''
  name: startOffset
  type: integer
- container: ''
  name: state
  type: string
- container: ''
  name: stringFilter
  type: string
- container: ''
  name: subjectToThresholding
  type: boolean
- container: ''
  name: timeZone
  type: string
- container: ''
  name: toValue
  type: string
- container: ''
  name: tokensPerDay
  type: reference
- container: ''
  name: tokensPerHour
  type: reference
- container: ''
  name: tokensPerProjectPerHour
  type: reference
- container: set
  name: totals
  type: reference
- container: ''
  name: upperCase
  type: reference
- container: ''
  name: value
  type: string
- container: set
  name: values
  type: string
property_count: 92
provider_name: Google Analytics
provider_slug: google-analytics
slug: google-analytics-data-api-context
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
- JSON-LD
- Linked Data
- Semantic Web
---
