---
class_count: 3
classes:
- PciDocumentInfo
- PciSigningRequest
- PciSigningResponse
context_file: json-ld/adyen-legal-entity-pci-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-pci-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Pci from Adyen.
layout: jsonld
name: Adyen Legal Entity Pci Context
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
  name: createdAt
  type: dateTime
- container: ''
  name: id
  type: string
- container: ''
  name: validUntil
  type: dateTime
- container: set
  name: pciTemplateReferences
  type: string
- container: ''
  name: signedBy
  type: string
- container: set
  name: pciQuestionnaireIds
  type: string
property_count: 6
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-pci-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
