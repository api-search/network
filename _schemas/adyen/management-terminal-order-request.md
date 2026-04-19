---
description: TerminalOrderRequest schema from Adyen API
layout: schema
name: TerminalOrderRequest
properties_list:
- description: The identification of the billing entity to use for the order.
  name: billingEntityId
  type: string
- description: The merchant-defined purchase order reference.
  name: customerOrderReference
  type: string
- description: The products included in the order.
  name: items
  type: array
- description: Type of order
  name: orderType
  type: string
- description: The identification of the shipping location to use for the order.
  name: shippingLocationId
  type: string
- description: The tax number of the billing entity.
  name: taxId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-terminal-order-request-schema.json
slug: management-terminal-order-request
tags:
- Payments
- Financial Services
- Fintech
title: TerminalOrderRequest
---
