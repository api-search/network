---
class_count: 3
classes:
- Advisory
- AffectedProduct
- Product
context_file: json-ld/palo-alto-security-advisory-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-security-advisory-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Security Advisory Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Security Advisory Api Context
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
  name: advisoryCount
  type: integer
- container: ''
  name: advisoryId
  type: string
- container: set
  name: affectedProducts
  type: reference
- container: ''
  name: cveId
  type: string
- container: ''
  name: cvssScore
  type: decimal
- container: ''
  name: cvssVector
  type: string
- container: ''
  name: cwe
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: exploitStatus
  type: string
- container: set
  name: fixedVersions
  type: string
- container: ''
  name: lastModifiedDate
  type: dateTime
- container: ''
  name: name
  type: string
- container: ''
  name: product
  type: string
- container: ''
  name: publishedDate
  type: dateTime
- container: set
  name: references
  type: reference
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: url
  type: reference
- container: ''
  name: version
  type: string
- container: set
  name: versions
  type: reference
- container: ''
  name: workarounds
  type: string
property_count: 22
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-security-advisory-api-context
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
