---
class_count: 6
classes:
- MetricDataObject
- CommonBlock
- MetricDataPoint
- name
- SummaryValue
- AcceptedResponse
context_file: json-ld/new-relic-metric-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/json-ld/new-relic-metric-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for New Relic Metric Api from New Relic.
layout: jsonld
name: New Relic Metric Api Context
namespaces:
- prefix: nr
  uri: https://docs.newrelic.com/docs/schemas/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: common
  type: string
- container: set
  name: metrics
  type: string
- container: ''
  name: timestamp
  type: integer
- container: ''
  name: interval.ms
  type: integer
- container: ''
  name: attributes
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: count
  type: decimal
- container: ''
  name: sum
  type: decimal
- container: ''
  name: min
  type: decimal
- container: ''
  name: max
  type: decimal
- container: ''
  name: requestId
  type: string
property_count: 12
provider_name: New Relic
provider_slug: new-relic
slug: new-relic-metric-api-context
tags:
- Analysis
- Analytics
- APM
- DevOps
- Infrastructure
- Monitoring
- Observability
- Performance
- Platform
- JSON-LD
- Linked Data
- Semantic Web
---
