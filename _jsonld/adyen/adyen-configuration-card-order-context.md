---
class_count: 3
classes:
- CardOrderItemDeliveryStatus
- CardOrderItem
- CardOrder
context_file: json-ld/adyen-configuration-card-order-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-card-order-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Card Order from Adyen.
layout: jsonld
name: Adyen Configuration Card Order Context
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
  name: errorMessage
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: trackingNumber
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: card
  type: string
- container: ''
  name: cardOrderItemId
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: id
  type: string
- container: ''
  name: paymentInstrumentId
  type: string
- container: ''
  name: pin
  type: string
- container: ''
  name: shippingMethod
  type: string
- container: ''
  name: beginDate
  type: dateTime
- container: ''
  name: cardManufacturingProfileId
  type: string
- container: ''
  name: closedDate
  type: dateTime
- container: ''
  name: endDate
  type: dateTime
- container: ''
  name: lockDate
  type: dateTime
- container: ''
  name: serviceCenter
  type: string
property_count: 17
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-card-order-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
