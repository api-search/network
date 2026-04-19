---
description: PaginatedGetCardOrderItemResponse schema from Adyen API
layout: schema
name: PaginatedGetCardOrderItemResponse
properties_list:
- description: List of card order items in the card order batch.
  name: data
  type: array
- description: Indicates whether there are more items on the next page.
  name: hasNext
  type: boolean
- description: Indicates whether there are more items on the previous page.
  name: hasPrevious
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-paginated-get-card-order-item-response-schema.json
slug: configuration-paginated-get-card-order-item-response
tags:
- Payments
- Financial Services
- Fintech
title: PaginatedGetCardOrderItemResponse
---
