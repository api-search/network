---
description: TerminalOrder schema from Adyen API
layout: schema
name: TerminalOrder
properties_list:
- description: The details of the entity that the order is billed to.
  name: billingEntity
  type: object
- description: The merchant-defined purchase order number. This will be printed on the packing list.
  name: customerOrderReference
  type: string
- description: The unique identifier of the order.
  name: id
  type: string
- description: The products included in the order.
  name: items
  type: array
- description: The date and time that the order was placed, in UTC ISO 8601 format. For example, "2011-12-03T10:15:30Z".
  name: orderDate
  type: string
- description: The details of the location where the order is shipped to.
  name: shippingLocation
  type: object
- description: The processing status of the order.
  name: status
  type: string
- description: The URL, provided by the carrier company, where the shipment can be tracked.
  name: trackingUrl
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-terminal-order-schema.json
slug: management-terminal-order
tags:
- Payments
- Financial Services
- Fintech
title: TerminalOrder
---
