---
class_count: 7
classes:
- ConstraintViolation
- EntityStub
- EventCollection
- EventIngestPayload
- EventIngestResultItem
- EventIngestResult
- Event
context_file: json-ld/dynatrace-events-api-v2-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/json-ld/dynatrace-events-api-v2-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Dynatrace Events Api V2 from Dynatrace.
layout: jsonld
name: Dynatrace Events Api V2 Context
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
  name: entityId
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: nextPageKey
  type: string
- container: ''
  name: totalCount
  type: integer
- container: ''
  name: pageSize
  type: integer
- container: set
  name: events
  type: ''
- container: ''
  name: eventType
  type: string
- container: ''
  name: timeout
  type: integer
- container: ''
  name: entitySelector
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: startTime
  type: integer
- container: ''
  name: endTime
  type: integer
- container: ''
  name: properties
  type: ''
- container: ''
  name: eventId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: reportCount
  type: integer
- container: set
  name: eventIngestResults
  type: ''
property_count: 22
provider_name: Dynatrace
provider_slug: dynatrace
slug: dynatrace-events-api-v2-context
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
