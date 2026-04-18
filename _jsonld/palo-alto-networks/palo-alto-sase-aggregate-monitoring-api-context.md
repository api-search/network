---
class_count: 3
classes:
- AggregationQuery
- AggregationResponse
- TenantSummary
context_file: json-ld/palo-alto-sase-aggregate-monitoring-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-aggregate-monitoring-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase Aggregate Monitoring Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase Aggregate Monitoring Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: childCount
  type: integer
- container: ''
  name: count
  type: integer
- container: set
  name: data
  type: reference
- container: ''
  name: depth
  type: integer
- container: ''
  name: displayName
  type: string
- container: ''
  name: end
  type: dateTime
- container: ''
  name: field
  type: string
- container: ''
  name: filter
  type: reference
- container: set
  name: groupBy
  type: string
- container: ''
  name: histogram
  type: reference
- container: ''
  name: interval
  type: string
- container: ''
  name: last
  type: string
- container: ''
  name: order
  type: string
- container: ''
  name: parentId
  type: string
- container: set
  name: sort
  type: reference
- container: ''
  name: start
  type: dateTime
- container: ''
  name: timeRange
  type: reference
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: total
  type: integer
- container: ''
  name: tsgId
  type: string
- container: ''
  name: values
  type: reference
property_count: 21
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-aggregate-monitoring-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---
