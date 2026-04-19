---
class_count: 2
classes:
- TaxInformation
- TaxReportingClassification
context_file: json-ld/adyen-legal-entity-tax-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-tax-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Tax from Adyen.
layout: jsonld
name: Adyen Legal Entity Tax Context
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
  name: country
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: businessType
  type: string
- container: ''
  name: financialInstitutionNumber
  type: string
- container: ''
  name: mainSourceOfIncome
  type: string
property_count: 6
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-tax-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
