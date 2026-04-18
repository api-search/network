---
class_count: 3
classes:
- PAN-OS Security Rule
- profile-setting
- profiles
context_file: json-ld/palo-alto-pan-os-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-pan-os-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Pan Os from Palo Alto Networks.
layout: jsonld
name: Palo Alto Pan Os Context
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
  name: action
  type: string
- container: set
  name: application
  type: string
- container: set
  name: data-filtering
  type: string
- container: ''
  name: description
  type: string
- container: set
  name: destination
  type: string
- container: ''
  name: disabled
  type: boolean
- container: set
  name: file-blocking
  type: string
- container: set
  name: from
  type: string
- container: set
  name: group
  type: string
- container: ''
  name: log-end
  type: boolean
- container: ''
  name: log-setting
  type: string
- container: ''
  name: log-start
  type: boolean
- container: ''
  name: name
  type: string
- container: ''
  name: negate-destination
  type: boolean
- container: ''
  name: negate-source
  type: boolean
- container: ''
  name: rule-type
  type: string
- container: ''
  name: schedule
  type: string
- container: set
  name: service
  type: string
- container: set
  name: source
  type: string
- container: set
  name: source-user
  type: string
- container: set
  name: spyware
  type: string
- container: set
  name: tag
  type: string
- container: set
  name: to
  type: string
- container: set
  name: url-filtering
  type: string
- container: set
  name: virus
  type: string
- container: set
  name: vulnerability
  type: string
- container: set
  name: wildfire-analysis
  type: string
property_count: 27
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-pan-os-context
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
