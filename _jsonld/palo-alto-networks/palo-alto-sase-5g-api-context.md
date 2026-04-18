---
class_count: 7
classes:
- NetworkSlice
- NetworkSliceRequest
- SecurityMetrics5G
- SecurityPolicy5G
- SecurityPolicy5GRequest
- Tenant5G
- Tenant5GRequest
context_file: json-ld/palo-alto-sase-5g-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-5g-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase 5G Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase 5G Api Context
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
  name: activeSubscribers
  type: integer
- container: ''
  name: appIdentification
  type: boolean
- container: set
  name: assignedSlices
  type: string
- container: ''
  name: bytesInspected
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: decryption
  type: boolean
- container: ''
  name: defaultPolicyId
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: end
  type: dateTime
- container: ''
  name: logForwarding
  type: boolean
- container: ''
  name: name
  type: string
- container: set
  name: perSliceMetrics
  type: reference
- container: ''
  name: period
  type: reference
- container: ''
  name: policyId
  type: string
- container: ''
  name: sd
  type: string
- container: ''
  name: securityPolicyId
  type: string
- container: ''
  name: sessions
  type: integer
- container: ''
  name: sliceId
  type: string
- container: ''
  name: sliceName
  type: string
- container: ''
  name: sliceType
  type: string
- container: ''
  name: sst
  type: integer
- container: ''
  name: start
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: tenantId
  type: string
- container: ''
  name: threatPrevention
  type: boolean
- container: ''
  name: threats
  type: integer
- container: ''
  name: threatsBlocked
  type: integer
- container: ''
  name: threatsDetected
  type: integer
- container: set
  name: timeSeries
  type: reference
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: totalSessions
  type: integer
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: urlFiltering
  type: boolean
property_count: 34
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-5g-api-context
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
