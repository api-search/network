---
class_count: 5
classes:
- AIProfile
- ContentScanResult
- ScanContent
- ScanRequest
- ScanResponse
context_file: json-ld/palo-alto-prisma-airs-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-airs-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Airs Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Airs Api Context
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
- container: ''
  name: aiProfile
  type: reference
- container: ''
  name: category
  type: string
- container: ''
  name: completedAt
  type: dateTime
- container: set
  name: contents
  type: reference
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: description
  type: string
- container: set
  name: detectionCategories
  type: reference
- container: ''
  name: dlp
  type: boolean
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: injection
  type: boolean
- container: ''
  name: profileId
  type: string
- container: ''
  name: profileName
  type: string
- container: ''
  name: prompt
  type: string
- container: ''
  name: promptDetected
  type: reference
- container: ''
  name: reportId
  type: string
- container: ''
  name: response
  type: string
- container: ''
  name: responseDetected
  type: reference
- container: set
  name: results
  type: reference
- container: ''
  name: scanCategory
  type: string
- container: ''
  name: scanId
  type: string
- container: ''
  name: sensitivity
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: toxicContent
  type: boolean
- container: ''
  name: trId
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: urlCats
  type: boolean
- container: ''
  name: verdict
  type: string
property_count: 28
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-airs-api-context
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
