---
class_count: 4
classes:
- DocumentPage
- DocumentReference
- Document
- description
context_file: json-ld/adyen-legal-entity-document-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-document-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Document from Adyen.
layout: jsonld
name: Adyen Legal Entity Document Context
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
  name: pageName
  type: string
- container: ''
  name: pageNumber
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: active
  type: boolean
- container: ''
  name: fileName
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: modificationDate
  type: dateTime
- container: set
  name: pages
  type: string
- container: ''
  name: attachment
  type: string
- container: set
  name: attachments
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: expiryDate
  type: string
- container: ''
  name: issuerCountry
  type: string
- container: ''
  name: issuerState
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: owner
  type: string
property_count: 16
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-document-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
