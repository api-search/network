---
class_count: 7
classes:
- ConstraintViolation
- LogAggregateGroup
- LogAggregateResult
- LogExportResult
- LogIngestRecord
- LogRecord
- LogRecordSearchResult
context_file: json-ld/dynatrace-log-monitoring-api-v2-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/json-ld/dynatrace-log-monitoring-api-v2-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Dynatrace Log Monitoring Api V2 from Dynatrace.
layout: jsonld
name: Dynatrace Log Monitoring Api V2 Context
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
  name: groupByFields
  type: ''
- container: ''
  name: count
  type: integer
- container: set
  name: results
  type: ''
- container: ''
  name: nextSliceKey
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: timestamp
  type: string
- container: ''
  name: log.source
  type: string
- container: ''
  name: dt.entity.host
  type: string
- container: ''
  name: additionalFields
  type: ''
property_count: 14
provider_name: Dynatrace
provider_slug: dynatrace
slug: dynatrace-log-monitoring-api-v2-context
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
