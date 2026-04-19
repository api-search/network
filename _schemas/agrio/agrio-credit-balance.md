---
description: Current API credit balance for the authenticated account.
layout: schema
name: Credit Balance
properties_list:
- description: Number of available credits remaining.
  name: balance
  type: integer
- description: Credit unit type.
  name: currency
  type: string
- description: Unique identifier for the API account.
  name: account_id
  type: string
provider_name: agrio
provider_slug: agrio
schema_file: json-schema/agrio-credit-balance-schema.json
slug: agrio-credit-balance
tags:
- Agriculture
- Plant Disease
- Pest Detection
- AI
- Crop Advisory
title: Credit Balance
---
