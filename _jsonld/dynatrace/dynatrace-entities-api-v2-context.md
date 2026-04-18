---
class_count: 10
classes:
- ConstraintViolation
- EntityCollection
- EntityLookupRequest
- Entity
- EntityTag
- EntityTypeCollection
- EntityTypeProperty
- EntityTypeRelationship
- EntityType
- ManagementZone
context_file: json-ld/dynatrace-entities-api-v2-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/json-ld/dynatrace-entities-api-v2-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Dynatrace Entities Api V2 from Dynatrace.
layout: jsonld
name: Dynatrace Entities Api V2 Context
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
  name: nextPageKey
  type: string
- container: ''
  name: totalCount
  type: integer
- container: ''
  name: pageSize
  type: integer
- container: set
  name: entities
  type: ''
- container: ''
  name: name
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: entityId
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: firstSeenTms
  type: integer
- container: ''
  name: lastSeenTms
  type: integer
- container: ''
  name: properties
  type: ''
- container: set
  name: tags
  type: ''
- container: set
  name: managementZones
  type: ''
- container: ''
  name: toRelationships
  type: ''
- container: ''
  name: fromRelationships
  type: ''
- container: ''
  name: context
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: stringRepresentation
  type: string
- container: set
  name: types
  type: ''
- container: ''
  name: id
  type: string
- container: set
  name: toTypes
  type: ''
- container: ''
  name: description
  type: string
property_count: 27
provider_name: Dynatrace
provider_slug: dynatrace
slug: dynatrace-entities-api-v2-context
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
