---
description: PaginatedGetCardOrderResponse schema from Adyen API
layout: schema
name: PaginatedGetCardOrderResponse
properties_list:
- description: Contains objects with information about card orders.
  name: cardOrders
  type: array
- description: Indicates whether there are more items on the next page.
  name: hasNext
  type: boolean
- description: Indicates whether there are more items on the previous page.
  name: hasPrevious
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-paginated-get-card-order-response-schema.json
slug: configuration-paginated-get-card-order-response
tags:
- Payments
- Financial Services
- Fintech
title: PaginatedGetCardOrderResponse
---
