---
description: ListTerminalsResponse schema from Adyen API
layout: schema
name: ListTerminalsResponse
properties_list:
- description: Pagination references.
  name: _links
  type: object
- description: The list of terminals and their details.
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
schema_file: json-schema/management-list-terminals-response-schema.json
slug: management-list-terminals-response
tags:
- Payments
- Financial Services
- Fintech
title: ListTerminalsResponse
---
