---
class_count: 1
classes:
- Transaction
context_file: json-ld/adyen-transfers-transaction-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-transfers-transaction-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Transfers Transaction from Adyen.
layout: jsonld
name: Adyen Transfers Transaction Context
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
  name: accountHolder
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: balanceAccount
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: bookingDate
  type: dateTime
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: id
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: transfer
  type: string
- container: ''
  name: valueDate
  type: dateTime
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-transfers-transaction-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
