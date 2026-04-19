---
class_count: 1
classes:
- DiagnosisRequest
context_file: json-ld/adyen-terminal-diagnosis-request-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-diagnosis-request-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Diagnosis Request from Adyen.
layout: jsonld
name: Adyen Terminal Diagnosis Request Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: POIID
  type: string
- container: ''
  name: HostDiagnosisFlag
  type: boolean
- container: set
  name: AcquirerID
  type: integer
property_count: 3
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-diagnosis-request-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
