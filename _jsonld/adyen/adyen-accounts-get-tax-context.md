---
class_count: 2
classes:
- GetTaxFormRequest
- GetTaxFormResponse
context_file: json-ld/adyen-accounts-get-tax-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-get-tax-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Get Tax from Adyen.
layout: jsonld
name: Adyen Accounts Get Tax Context
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
  name: accountHolderCode
  type: string
- container: ''
  name: formType
  type: string
- container: ''
  name: year
  type: integer
- container: ''
  name: content
  type: string
- container: ''
  name: contentType
  type: string
- container: set
  name: invalidFields
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-get-tax-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
