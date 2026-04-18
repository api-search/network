---
class_count: 3
classes:
- EventDataPayload
- LogDataPayload
- XdrDataPayload
context_file: json-ld/palo-alto-cortex-xsiam-data-ingestion-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xsiam-data-ingestion-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Cortex Xsiam Data Ingestion from Palo Alto Networks.
layout: jsonld
name: Palo Alto Cortex Xsiam Data Ingestion Context
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
  name: dataset
  type: string
- container: ''
  name: eventId
  type: string
- container: ''
  name: logType
  type: string
- container: ''
  name: product
  type: string
- container: ''
  name: rawLog
  type: string
- container: ''
  name: tenantId
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: vendor
  type: string
property_count: 8
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-cortex-xsiam-data-ingestion-context
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
