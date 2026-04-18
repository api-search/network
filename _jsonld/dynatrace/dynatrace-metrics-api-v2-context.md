---
class_count: 8
classes:
- ConstraintViolation
- MetricData
- MetricDefaultAggregation
- MetricDescriptorCollection
- MetricDescriptor
- MetricDimensionDefinition
- MetricSeriesCollection
- MetricSeries
context_file: json-ld/dynatrace-metrics-api-v2-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/json-ld/dynatrace-metrics-api-v2-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Dynatrace Metrics Api V2 from Dynatrace.
layout: jsonld
name: Dynatrace Metrics Api V2 Context
namespaces:
- prefix: dt
  uri: https://dt.dynatrace.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: path
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: parameterLocation
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: resolution
  type: string
- container: ''
  name: nextPageKey
  type: string
- container: ''
  name: totalCount
  type: integer
- container: set
  name: result
  type: ''
- container: ''
  name: type
  type: string
- container: ''
  name: parameter
  type: decimal
- container: set
  name: metrics
  type: ''
- container: ''
  name: metricId
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: dduBillable
  type: boolean
- container: ''
  name: created
  type: integer
- container: ''
  name: lastWritten
  type: integer
- container: set
  name: entityType
  type: ''
- container: set
  name: aggregationTypes
  type: ''
- container: set
  name: dimensionDefinitions
  type: ''
- container: set
  name: transformations
  type: ''
- container: ''
  name: defaultAggregation
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: name
  type: string
- container: set
  name: data
  type: ''
- container: ''
  name: dimensionMap
  type: ''
- container: set
  name: dimensions
  type: ''
- container: set
  name: timestamps
  type: ''
- container: set
  name: values
  type: ''
property_count: 30
provider_name: Dynatrace
provider_slug: dynatrace
slug: dynatrace-metrics-api-v2-context
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
- JSON-LD
- Linked Data
- Semantic Web
---
