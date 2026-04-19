---
class_count: 3
classes:
- Trust
- description
- name
context_file: json-ld/adyen-legal-entity-trust-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-trust-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Trust from Adyen.
layout: jsonld
name: Adyen Legal Entity Trust Context
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
  name: countryOfGoverningLaw
  type: string
- container: ''
  name: dateOfIncorporation
  type: string
- container: ''
  name: doingBusinessAs
  type: string
- container: ''
  name: principalPlaceOfBusiness
  type: string
- container: ''
  name: registeredAddress
  type: string
- container: ''
  name: registrationNumber
  type: string
- container: set
  name: taxInformation
  type: string
- container: ''
  name: type
  type: string
- container: set
  name: undefinedBeneficiaryInfo
  type: string
- container: ''
  name: vatAbsenceReason
  type: string
- container: ''
  name: vatNumber
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-trust-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
