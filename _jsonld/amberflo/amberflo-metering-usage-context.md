---
class_count: 3
classes:
- UsageRecord
- UsageQueryResponse
- UsageQueryRequest
context_file: json-ld/amberflo-metering-usage-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/json-ld/amberflo-metering-usage-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amberflo Metering Usage from Amberflo.
layout: jsonld
name: Amberflo Metering Usage Context
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
  name: groupInfo
  type: reference
- container: set
  name: records
  type: reference
- container: ''
  name: clientMeters
  type: reference
- container: ''
  name: meterApiName
  type: string
- container: ''
  name: startTimeInSeconds
  type: integer
- container: ''
  name: endTimeInSeconds
  type: integer
- container: ''
  name: aggregation
  type: string
- container: ''
  name: timeGroupingInterval
  type: string
- container: set
  name: groupBy
  type: string
- container: set
  name: customerFilter
  type: string
- container: ''
  name: filter
  type: reference
property_count: 11
provider_name: Amberflo
provider_slug: amberflo
slug: amberflo-metering-usage-context
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
