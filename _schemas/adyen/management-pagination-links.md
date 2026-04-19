---
description: PaginationLinks schema from Adyen API
layout: schema
name: PaginationLinks
properties_list:
- description: The first page.
  name: first
  type: object
- description: The last page.
  name: last
  type: object
- description: The next page. Only present if there is a next page.
  name: next
  type: object
- description: The previous page. Only present if there is a previous page.
  name: prev
  type: object
- description: The current page.
  name: self
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-pagination-links-schema.json
slug: management-pagination-links
tags:
- Payments
- Financial Services
- Fintech
title: PaginationLinks
---
