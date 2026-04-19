---
class_count: 3
classes:
- Transaction
- Card
- FileObject
context_file: json-ld/affirm-direct-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/json-ld/affirm-direct-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Affirm Direct from affirm.
layout: jsonld
name: Affirm Direct Context
namespaces:
- prefix: affirm
  uri: https://affirm.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: checkoutId
  type: string
- container: ''
  name: orderId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: amount
  type: integer
- container: ''
  name: amountRefunded
  type: integer
- container: ''
  name: currency
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: authorizationExpiration
  type: dateTime
- container: ''
  name: number
  type: string
- container: ''
  name: cvv
  type: string
- container: ''
  name: expiration
  type: string
- container: ''
  name: billing
  type: reference
- container: ''
  name: address
  type: reference
- container: ''
  name: line1
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: zipcode
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: filename
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: contentType
  type: string
- container: ''
  name: purpose
  type: string
property_count: 23
provider_name: affirm
provider_slug: affirm
slug: affirm-direct-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
