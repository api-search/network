---
description: ''
layout: schema
name: PendingProductOrder
properties_list:
- description: Type of product order, e.g. 'Add' or 'Remove'.
  name: type
  type: string
- description: Status of the pending product order.
  name: status
  type: string
- description: Date and time when product was ordered.
  name: requested
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-procure-to-pay-scim-pending-product-order-schema.json
slug: factset-procure-to-pay-scim-pending-product-order
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: PendingProductOrder
---
