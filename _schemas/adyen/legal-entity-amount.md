---
description: Amount schema from Adyen API
layout: schema
name: Amount
properties_list:
- description: The type of currency. Must be EUR (or EUR equivalent)
  name: currency
  type: string
- description: Total value of amount. Must be >= 0
  name: value
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-amount-schema.json
slug: legal-entity-amount
tags:
- Payments
- Financial Services
- Fintech
title: Amount
---
