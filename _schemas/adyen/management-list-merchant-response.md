---
description: ListMerchantResponse schema from Adyen API
layout: schema
name: ListMerchantResponse
properties_list:
- description: Pagination references.
  name: _links
  type: object
- description: The list of merchant accounts.
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
schema_file: json-schema/management-list-merchant-response-schema.json
slug: management-list-merchant-response
tags:
- Payments
- Financial Services
- Fintech
title: ListMerchantResponse
---
