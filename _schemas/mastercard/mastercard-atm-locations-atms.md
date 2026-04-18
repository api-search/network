---
description: ''
layout: schema
name: Atms
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
- description: The total number of ATMs available to be retrieved
  name: total
  type: integer
- description: The list of ATMs retrieved
  name: atms
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-atm-locations-atms-schema.json
slug: mastercard-atm-locations-atms
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Atms
---
