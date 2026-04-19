---
class_count: 1
classes:
- GenericResponse
context_file: json-ld/adyen-accounts-generic-response-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-generic-response-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Generic Response from Adyen.
layout: jsonld
name: Adyen Accounts Generic Response Context
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
  name: invalidFields
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 3
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-generic-response-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
