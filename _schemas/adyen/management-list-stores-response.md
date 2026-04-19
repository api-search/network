---
description: ListStoresResponse schema from Adyen API
layout: schema
name: ListStoresResponse
properties_list:
- description: Pagination references.
  name: _links
  type: object
- description: List of stores
  name: data
  type: array
- description: Total number of items.
  name: itemsTotal
  type: integer
- description: Total number of pages.
  name: pagesTotal
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-list-stores-response-schema.json
slug: management-list-stores-response
tags:
- Payments
- Financial Services
- Fintech
title: ListStoresResponse
---
