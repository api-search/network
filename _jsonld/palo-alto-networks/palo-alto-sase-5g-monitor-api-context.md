---
class_count: 5
classes:
- CountFilterRequest
- IncidentsCountRequest
- MappingRequest
- ThroughputRequest
- TrendRequest
context_file: json-ld/palo-alto-sase-5g-monitor-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-5g-monitor-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase 5G Monitor Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase 5G Monitor Api Context
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
  name: alias
  type: string
- container: ''
  name: enableEmptyInterval
  type: boolean
- container: ''
  name: filter
  type: reference
- container: ''
  name: function
  type: string
- container: ''
  name: histogram
  type: reference
- container: ''
  name: operator
  type: string
- container: ''
  name: pageNum
  type: integer
- container: ''
  name: pageSize
  type: integer
- container: set
  name: properties
  type: reference
- container: ''
  name: property
  type: string
- container: ''
  name: range
  type: string
- container: ''
  name: region
  type: string
- container: set
  name: rules
  type: reference
- container: ''
  name: searchKey
  type: string
- container: set
  name: tenant
  type: string
- container: ''
  name: value
  type: string
- container: set
  name: values
  type: reference
property_count: 17
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-5g-monitor-api-context
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
