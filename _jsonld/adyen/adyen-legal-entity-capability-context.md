---
class_count: 4
classes:
- CapabilityProblemEntity-recursive
- CapabilityProblemEntity
- CapabilityProblem
- CapabilitySettings
context_file: json-ld/adyen-legal-entity-capability-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-capability-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Capability from Adyen.
layout: jsonld
name: Adyen Legal Entity Capability Context
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
- container: set
  name: documents
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: entity
  type: string
- container: set
  name: verificationErrors
  type: string
- container: ''
  name: amountPerIndustry
  type: reference
- container: ''
  name: authorizedCardUsers
  type: boolean
- container: set
  name: fundingSource
  type: string
- container: ''
  name: interval
  type: string
- container: ''
  name: maxAmount
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-capability-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
