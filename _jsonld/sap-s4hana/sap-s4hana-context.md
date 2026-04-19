---
class_count: 10
classes:
- Order
- OrderItem
- Organization
- Product
- PriceSpecification
- name
- description
- identifier
- customer
- orderedItem
context_file: json-ld/sap-s4hana-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/sap-s4hana/refs/heads/main/json-ld/sap-s4hana-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Sap S4Hana from SAP S/4HANA.
layout: jsonld
name: Sap S4Hana Context
namespaces:
- prefix: sap
  uri: https://api.sap.com/ns/s4hana/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: rdfs
  uri: http://www.w3.org/2000/01/rdf-schema#
- prefix: skos
  uri: http://www.w3.org/2004/02/skos/core#
- prefix: gr
  uri: http://purl.org/goodrelations/v1#
properties:
- container: ''
  name: SalesOrder
  type: reference
- container: ''
  name: SalesOrderItem
  type: reference
- container: ''
  name: SalesOrderPartner
  type: reference
- container: ''
  name: SalesOrderPricingElement
  type: reference
- container: ''
  name: SalesOrderScheduleLine
  type: reference
- container: ''
  name: SalesOrderTextRecord
  type: reference
- container: ''
  name: url
  type: anyURI
- container: ''
  name: dateCreated
  type: date
- container: ''
  name: dateModified
  type: date
- container: ''
  name: orderNumber
  type: string
- container: ''
  name: orderDate
  type: date
- container: ''
  name: orderStatus
  type: string
- container: ''
  name: totalPrice
  type: decimal
- container: ''
  name: priceCurrency
  type: string
property_count: 14
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
slug: sap-s4hana-context
tags:
- Business Applications
- Cloud
- Enterprise Resource Planning
- ERP
- Finance
- Human Resources
- Inventory
- Logistics
- Manufacturing
- Plant Maintenance
- Procurement
- S/4HANA
- Sales
- SAP
- JSON-LD
- Linked Data
- Semantic Web
---
