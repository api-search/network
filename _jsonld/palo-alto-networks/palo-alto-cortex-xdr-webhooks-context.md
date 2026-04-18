---
class_count: 2
classes:
- AlertPayload
- IncidentPayload
context_file: json-ld/palo-alto-cortex-xdr-webhooks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xdr-webhooks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Cortex Xdr Webhooks from Palo Alto Networks.
layout: jsonld
name: Palo Alto Cortex Xdr Webhooks Context
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
  name: alertCount
  type: integer
- container: set
  name: alertSources
  type: string
- container: ''
  name: assignedUserMail
  type: string
- container: ''
  name: creationTime
  type: integer
- container: ''
  name: description
  type: string
- container: ''
  name: incidentId
  type: string
- container: ''
  name: modificationTime
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
property_count: 10
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-cortex-xdr-webhooks-context
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
