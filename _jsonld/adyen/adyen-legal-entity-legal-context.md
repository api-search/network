---
class_count: 6
classes:
- LegalEntityAssociation
- LegalEntityCapability
- LegalEntityInfoRequiredType
- LegalEntityInfo
- LegalEntity
- name
context_file: json-ld/adyen-legal-entity-legal-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-legal-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Legal from Adyen.
layout: jsonld
name: Adyen Legal Entity Legal Context
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
  name: associatorId
  type: string
- container: ''
  name: entityType
  type: string
- container: ''
  name: jobTitle
  type: string
- container: ''
  name: legalEntityId
  type: string
- container: set
  name: settlorExemptionReason
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: allowed
  type: boolean
- container: ''
  name: allowedLevel
  type: string
- container: ''
  name: allowedSettings
  type: string
- container: ''
  name: requested
  type: boolean
- container: ''
  name: requestedLevel
  type: string
- container: ''
  name: requestedSettings
  type: string
- container: set
  name: transferInstruments
  type: string
- container: ''
  name: verificationStatus
  type: string
- container: ''
  name: capabilities
  type: reference
- container: set
  name: entityAssociations
  type: string
- container: ''
  name: individual
  type: string
- container: ''
  name: organization
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: soleProprietorship
  type: string
- container: ''
  name: trust
  type: string
- container: ''
  name: unincorporatedPartnership
  type: string
- container: ''
  name: verificationPlan
  type: string
- container: set
  name: documentDetails
  type: string
- container: set
  name: documents
  type: string
- container: ''
  name: id
  type: string
- container: set
  name: problems
  type: string
- container: set
  name: verificationDeadlines
  type: string
property_count: 28
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-legal-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
