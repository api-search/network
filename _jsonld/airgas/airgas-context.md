---
class_count: 5
classes:
- Product
- Order
- Account
- name
- description
context_file: json-ld/airgas-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/airgas/refs/heads/main/json-ld/airgas-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Airgas from Airgas.
layout: jsonld
name: Airgas Context
namespaces:
- prefix: airgas
  uri: https://airgas.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: productNumber
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: gasType
  type: string
- container: ''
  name: grade
  type: string
- container: ''
  name: price
  type: decimal
- container: ''
  name: orderNumber
  type: string
- container: ''
  name: accountNumber
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: orderDate
  type: dateTime
- container: ''
  name: deliveryDate
  type: date
- container: ''
  name: totalAmount
  type: decimal
- container: ''
  name: companyName
  type: string
- container: ''
  name: accountType
  type: string
- container: ''
  name: creditLimit
  type: decimal
- container: ''
  name: paymentTerms
  type: string
- container: ''
  name: isActive
  type: boolean
property_count: 16
provider_name: Airgas
provider_slug: airgas
slug: airgas-context
tags:
- Industrial Gases
- Welding
- Safety
- B2B
- Supply Chain
- Manufacturing
- Healthcare
- JSON-LD
- Linked Data
- Semantic Web
---
