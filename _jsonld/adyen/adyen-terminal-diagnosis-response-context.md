---
class_count: 1
classes:
- DiagnosisResponse
context_file: json-ld/adyen-terminal-diagnosis-response-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-diagnosis-response-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Diagnosis Response from Adyen.
layout: jsonld
name: Adyen Terminal Diagnosis Response Context
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
  name: Response
  type: string
- container: set
  name: LoggedSaleID
  type: string
- container: ''
  name: POIStatus
  type: string
- container: set
  name: HostStatus
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-diagnosis-response-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
