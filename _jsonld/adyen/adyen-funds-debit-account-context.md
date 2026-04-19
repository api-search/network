---
class_count: 3
classes:
- DebitAccountHolderRequest
- DebitAccountHolderResponse
- description
context_file: json-ld/adyen-funds-debit-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-funds-debit-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Funds Debit Account from Adyen.
layout: jsonld
name: Adyen Funds Debit Account Context
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
  name: amount
  type: string
- container: ''
  name: bankAccountUUID
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: set
  name: splits
  type: string
- container: set
  name: invalidFields
  type: string
- container: set
  name: merchantReferences
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 9
provider_name: Adyen
provider_slug: adyen
slug: adyen-funds-debit-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
