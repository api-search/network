---
class_count: 3
classes:
- TransferInstrumentInfo
- TransferInstrumentReference
- TransferInstrument
context_file: json-ld/adyen-legal-entity-transfer-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-transfer-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Transfer from Adyen.
layout: jsonld
name: Adyen Legal Entity Transfer Context
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
  name: bankAccount
  type: string
- container: ''
  name: legalEntityId
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: accountIdentifier
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: realLastFour
  type: string
- container: ''
  name: trustedSource
  type: boolean
- container: ''
  name: capabilities
  type: reference
- container: set
  name: documentDetails
  type: string
- container: set
  name: problems
  type: string
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-transfer-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
