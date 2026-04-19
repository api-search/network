---
description: TransactionSearchResponse schema from Adyen API
layout: schema
name: TransactionSearchResponse
properties_list:
- description: Contains links to the next and previous page whenever applicable.
  name: _links
  type: object
- description: Contains the transactions that match the query parameters.
  name: data
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-transaction-search-response-schema.json
slug: transfers-transaction-search-response
tags:
- Payments
- Financial Services
- Fintech
title: TransactionSearchResponse
---
