---
class_count: 4
classes:
- BusinessLineInfo
- BusinessLineInfoUpdate
- BusinessLine
- BusinessLines
context_file: json-ld/adyen-legal-entity-business-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-business-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Business from Adyen.
layout: jsonld
name: Adyen Legal Entity Business Context
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
  name: capability
  type: string
- container: ''
  name: industryCode
  type: string
- container: ''
  name: legalEntityId
  type: string
- container: set
  name: salesChannels
  type: string
- container: ''
  name: service
  type: string
- container: ''
  name: sourceOfFunds
  type: string
- container: set
  name: webData
  type: string
- container: ''
  name: webDataExemption
  type: string
- container: ''
  name: id
  type: string
- container: set
  name: problems
  type: string
- container: set
  name: businessLines
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-business-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
