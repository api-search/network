---
class_count: 5
classes:
- LegalArrangementDetail
- LegalArrangementEntityDetail
- LegalArrangementRequest
- name
- email
context_file: json-ld/adyen-accounts-legal-arrangement-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-legal-arrangement-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Legal Arrangement from Adyen.
layout: jsonld
name: Adyen Accounts Legal Arrangement Context
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
  name: address
  type: string
- container: ''
  name: legalArrangementCode
  type: string
- container: set
  name: legalArrangementEntities
  type: string
- container: ''
  name: legalArrangementReference
  type: string
- container: ''
  name: legalForm
  type: string
- container: ''
  name: registrationNumber
  type: string
- container: ''
  name: taxNumber
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: businessDetails
  type: string
- container: ''
  name: fullPhoneNumber
  type: string
- container: ''
  name: individualDetails
  type: string
- container: ''
  name: legalArrangementEntityCode
  type: string
- container: ''
  name: legalArrangementEntityReference
  type: string
- container: set
  name: legalArrangementMembers
  type: string
- container: ''
  name: legalEntityType
  type: string
- container: ''
  name: phoneNumber
  type: string
- container: ''
  name: webAddress
  type: string
- container: set
  name: legalArrangementEntityCodes
  type: string
property_count: 18
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-legal-arrangement-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
