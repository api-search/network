---
class_count: 3
classes:
- IndustrialGasProduct
- GasOrder
- TankTelemetry
context_file: json-ld/airproducts-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/air-products-and-chemicals/refs/heads/main/json-ld/airproducts-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Airproducts from Air Products and Chemicals.
layout: jsonld
name: Airproducts Context
namespaces:
- prefix: airproducts
  uri: https://airproducts.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: productId
  type: string
- container: ''
  name: chemicalFormula
  type: string
- container: ''
  name: purityGrade
  type: string
- container: ''
  name: purityPercent
  type: decimal
- container: ''
  name: orderId
  type: string
- container: ''
  name: quantity
  type: decimal
- container: ''
  name: deliveryDate
  type: date
- container: ''
  name: tankId
  type: string
- container: ''
  name: levelPercent
  type: decimal
- container: ''
  name: timestamp
  type: dateTime
property_count: 12
provider_name: Air Products and Chemicals
provider_slug: air-products-and-chemicals
slug: airproducts-context
tags:
- Industrial Gases
- Chemicals
- Energy
- Manufacturing
- Hydrogen
- Enterprise
- JSON-LD
- Linked Data
- Semantic Web
---
