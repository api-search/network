---
description: Shipment record for an order
layout: schema
name: Shipment
properties_list:
- description: Shipment identifier
  name: shipmentId
  type: string
- description: Associated order ID
  name: orderId
  type: string
- description: Shipping carrier name
  name: carrier
  type: string
- description: Carrier PRO/tracking number
  name: proNumber
  type: string
- description: Carrier tracking URL
  name: trackingUrl
  type: string
- description: ''
  name: shipDate
  type: string
- description: ''
  name: estimatedDeliveryDate
  type: string
- description: Shipment weight in lbs
  name: weight
  type: number
- description: Line items in this shipment
  name: lineItems
  type: array
provider_name: acuity-brands
provider_slug: acuity-brands
schema_file: json-schema/acuity-brands-shipment-schema.json
slug: acuity-brands-shipment
tags: []
title: Shipment
---
