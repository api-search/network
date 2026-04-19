---
class_count: 14
classes:
- Delivery
- Order
- Invoice
- InvoiceList
- OrderItem
- Product
- OrderList
- CreateOrderRequest
- ProductPrice
- DeliveryList
- ProductList
- ShippingAddress
- description
- name
context_file: json-ld/3m-partner-supplier-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/3m/refs/heads/main/json-ld/3m-partner-supplier-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for 3M Partner Supplier Api from 3M.
layout: jsonld
name: 3M Partner Supplier Api Context
namespaces:
- prefix: threeem
  uri: https://api.3m.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: availability
  type: string
- container: ''
  name: carrier
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: currency
  type: string
- container: set
  name: deliveries
  type: ''
- container: ''
  name: deliveryId
  type: string
- container: ''
  name: dueDate
  type: date
- container: ''
  name: effectiveDate
  type: date
- container: ''
  name: estimatedDelivery
  type: date
- container: ''
  name: expirationDate
  type: date
- container: ''
  name: invoiceDate
  type: date
- container: ''
  name: invoiceId
  type: string
- container: set
  name: invoices
  type: ''
- container: set
  name: items
  type: ''
- container: ''
  name: orderId
  type: string
- container: set
  name: orders
  type: ''
- container: ''
  name: pricingTier
  type: string
- container: ''
  name: productId
  type: string
- container: set
  name: products
  type: ''
- container: ''
  name: quantity
  type: integer
- container: ''
  name: shippedAt
  type: dateTime
- container: ''
  name: sku
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: street
  type: string
- container: ''
  name: totalAmount
  type: decimal
- container: ''
  name: trackingNumber
  type: string
- container: ''
  name: unitPrice
  type: decimal
- container: ''
  name: zip
  type: string
property_count: 32
provider_name: 3M
provider_slug: 3m
slug: 3m-partner-supplier-api-context
tags:
- Industrial
- Manufacturing
- Supply Chain
- JSON-LD
- Linked Data
- Semantic Web
---
