---
class_count: 3
classes:
- MeterEvent
- MeterDefinition
- MeterDefinitionRequest
context_file: json-ld/amberflo-metering-meter-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/json-ld/amberflo-metering-meter-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amberflo Metering Meter from Amberflo.
layout: jsonld
name: Amberflo Metering Meter Context
namespaces:
- prefix: amberflo
  uri: https://amberflo.io/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: meterApiName
  type: string
- container: ''
  name: customerId
  type: string
- container: ''
  name: meterValue
  type: decimal
- container: ''
  name: meterTimeInMillis
  type: integer
- container: ''
  name: uniqueId
  type: string
- container: set
  name: dimensions
  type: string
- container: ''
  name: values
  type: reference
- container: ''
  name: displayName
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: type
  type: string
property_count: 10
provider_name: Amberflo
provider_slug: amberflo
slug: amberflo-metering-meter-context
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
- JSON-LD
- Linked Data
- Semantic Web
---
