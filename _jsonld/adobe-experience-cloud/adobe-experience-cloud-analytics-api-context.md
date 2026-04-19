---
class_count: 18
classes:
- Project
- UserList
- User
- CalculatedMetricList
- ReportSuite
- SegmentList
- ProjectList
- CalculatedMetric
- ReportResponse
- ReportRequest
- ReportSuiteList
- Metric
- DateRangeList
- Dimension
- Segment
- name
- description
- email
context_file: json-ld/adobe-experience-cloud-analytics-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/json-ld/adobe-experience-cloud-analytics-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Experience Cloud Analytics Api from Adobe Experience Cloud.
layout: jsonld
name: Adobe Experience Cloud Analytics Api Context
namespaces:
- prefix: aec
  uri: https://developer.adobe.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: owner
  type: reference
- container: ''
  name: modified
  type: dateTime
- container: set
  name: content
  type: string
- container: ''
  name: loginId
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: admin
  type: boolean
- container: ''
  name: totalElements
  type: integer
- container: ''
  name: totalPages
  type: integer
- container: ''
  name: rsid
  type: string
- container: ''
  name: polarity
  type: string
- container: ''
  name: definition
  type: reference
- container: ''
  name: currency
  type: string
- container: ''
  name: timezone
  type: integer
- container: ''
  name: calendarType
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: firstPage
  type: boolean
- container: ''
  name: lastPage
  type: boolean
- container: ''
  name: numberOfElements
  type: integer
- container: set
  name: rows
  type: string
- container: ''
  name: itemId
  type: string
- container: ''
  name: value
  type: string
- container: set
  name: data
  type: decimal
- container: set
  name: globalFilters
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: dateRange
  type: string
- container: ''
  name: metricContainer
  type: reference
- container: set
  name: metrics
  type: string
- container: ''
  name: dimension
  type: string
- container: ''
  name: settings
  type: reference
- container: ''
  name: limit
  type: integer
- container: ''
  name: page
  type: integer
- container: ''
  name: segmentable
  type: boolean
property_count: 34
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
slug: adobe-experience-cloud-analytics-api-context
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
- JSON-LD
- Linked Data
- Semantic Web
---
