---
class_count: 0
classes: []
context_file: json-ld/anchore-enterprise-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/json-ld/anchore-enterprise-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Anchore Enterprise Api from Anchore.
layout: jsonld
name: Anchore Enterprise Api Context
namespaces:
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
- prefix: anchore
  uri: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/vocabulary/
properties:
- container: ''
  name: imageDigest
  type: string
- container: ''
  name: analysisStatus
  type: string
- container: ''
  name: imageStatus
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: vuln
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: package
  type: string
- container: ''
  name: packageVersion
  type: string
- container: ''
  name: fix
  type: string
- container: set
  name: components
  type: ''
- container: ''
  name: bomFormat
  type: string
- container: ''
  name: purl
  type: reference
- container: set
  name: licenses
  type: ''
property_count: 14
provider_name: Anchore
provider_slug: anchore
slug: anchore-enterprise-api-context
tags:
- Container Security
- Containers
- SBOM
- Software Supply Chain
- Vulnerability Scanning
- JSON-LD
- Linked Data
- Semantic Web
---
