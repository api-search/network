---
description: ListWebhooksResponse schema from Adyen API
layout: schema
name: ListWebhooksResponse
properties_list:
- description: Pagination references.
  name: _links
  type: object
- description: Reference to the account.
  name: accountReference
  type: string
- description: The list of webhooks configured for this account.
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
schema_file: json-schema/management-list-webhooks-response-schema.json
slug: management-list-webhooks-response
tags:
- Payments
- Financial Services
- Fintech
title: ListWebhooksResponse
---
