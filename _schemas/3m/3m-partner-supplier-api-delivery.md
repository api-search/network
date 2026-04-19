---
description: Delivery tracking record for an order
layout: schema
name: Delivery
properties_list:
- description: Unique delivery identifier
  name: deliveryId
  type: string
- description: Associated order identifier
  name: orderId
  type: string
- description: Shipping carrier name
  name: carrier
  type: string
- description: Carrier tracking number
  name: trackingNumber
  type: string
- description: Current delivery status
  name: status
  type: string
- description: Estimated delivery date
  name: estimatedDelivery
  type: string
- description: Timestamp when the shipment was dispatched
  name: shippedAt
  type: string
provider_name: 3M
provider_slug: 3m
schema_file: json-schema/3m-partner-supplier-api-delivery-schema.json
slug: 3m-partner-supplier-api-delivery
tags:
- Industrial
- Manufacturing
- Supply Chain
title: Delivery
---
