---
class_count: 11
classes:
- AlertingProfileStub
- CommentCollection
- CommentRequestBody
- Comment
- ConstraintViolation
- EntityStub
- ManagementZone
- ProblemCloseRequest
- ProblemCloseResult
- ProblemCollection
- Problem
context_file: json-ld/dynatrace-problems-api-v2-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/json-ld/dynatrace-problems-api-v2-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Dynatrace Problems Api V2 from Dynatrace.
layout: jsonld
name: Dynatrace Problems Api V2 Context
namespaces:
- prefix: dt
  uri: https://dt.dynatrace.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: nextPageKey
  type: string
- container: ''
  name: totalCount
  type: integer
- container: set
  name: comments
  type: ''
- container: ''
  name: message
  type: string
- container: ''
  name: context
  type: string
- container: ''
  name: createdAtTimestamp
  type: integer
- container: ''
  name: authorName
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: path
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
  name: type
  type: string
- container: ''
  name: problemId
  type: string
- container: ''
  name: closing
  type: boolean
- container: ''
  name: pageSize
  type: integer
- container: set
  name: problems
  type: ''
- container: ''
  name: displayId
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: severityLevel
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: startTime
  type: integer
- container: ''
  name: endTime
  type: integer
- container: set
  name: affectedEntities
  type: ''
- container: set
  name: impactedEntities
  type: ''
- container: ''
  name: rootCauseEntity
  type: string
- container: set
  name: managementZones
  type: ''
- container: set
  name: problemFilters
  type: ''
property_count: 30
provider_name: Dynatrace
provider_slug: dynatrace
slug: dynatrace-problems-api-v2-context
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
