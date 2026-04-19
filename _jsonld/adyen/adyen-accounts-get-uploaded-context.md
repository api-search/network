---
class_count: 2
classes:
- GetUploadedDocumentsRequest
- GetUploadedDocumentsResponse
context_file: json-ld/adyen-accounts-get-uploaded-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-get-uploaded-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Get Uploaded from Adyen.
layout: jsonld
name: Adyen Accounts Get Uploaded Context
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
  name: bankAccountUUID
  type: string
- container: ''
  name: shareholderCode
  type: string
- container: set
  name: documentDetails
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
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-get-uploaded-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
