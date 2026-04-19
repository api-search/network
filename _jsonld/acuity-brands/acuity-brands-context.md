---
class_count: 50
classes:
- InventoryItem
- InventoryList
- Order
- OrderList
- Shipment
- ShipmentList
- CatalogItem
- CatalogItemList
- Webpage
- WebpageList
- productNumber
- description
- brand
- totalQuantity
- warehouses
- items
- total
- cursor
- orderId
- purchaseOrderNumber
- status
- lineItems
- totalAmount
- shipToAddress
- shipmentId
- carrier
- proNumber
- trackingUrl
- weight
- name
- category
- subcategory
- specifications
- certifications
- listPrice
- upc
- imageUrl
- dataSheetUrl
- pageId
- url
- title
- type
- metaDescription
- orders
- shipments
- pages
- quantity
- unitPrice
- lineNumber
- quantityShipped
context_file: json-ld/acuity-brands-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/acuity-brands/refs/heads/main/json-ld/acuity-brands-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Acuity Brands from acuity-brands.
layout: jsonld
name: Acuity Brands Context
namespaces:
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: acuity
  uri: https://vocab.api-evangelist.com/acuity-brands/
properties:
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: orderDate
  type: date
- container: ''
  name: estimatedShipDate
  type: date
- container: ''
  name: actualShipDate
  type: date
- container: ''
  name: shipDate
  type: date
- container: ''
  name: estimatedDeliveryDate
  type: date
- container: ''
  name: lastModified
  type: dateTime
property_count: 7
provider_name: acuity-brands
provider_slug: acuity-brands
slug: acuity-brands-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
