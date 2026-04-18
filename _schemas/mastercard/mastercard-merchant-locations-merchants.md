---
description: ''
layout: schema
name: Merchants
properties_list:
- description: The number of items in the retrieved data set
  name: count
  type: integer
- description: The number of items requested to be retrieved
  name: limit
  type: integer
- description: The page offset used for the query
  name: offset
  type: integer
- description: The total number of merchants available to be retrieved
  name: total
  type: integer
- description: The list of merchants retrieved
  name: merchants
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-merchant-locations-merchants-schema.json
slug: mastercard-merchant-locations-merchants
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Merchants
---
