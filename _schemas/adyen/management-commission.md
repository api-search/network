---
description: Commission schema from Adyen API
layout: schema
name: Commission
properties_list:
- description: A fixed commission fee, in minor units.
  name: fixedAmount
  type: integer
- description: A variable commission fee, in basis points.
  name: variablePercentage
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-commission-schema.json
slug: management-commission
tags:
- Payments
- Financial Services
- Fintech
title: Commission
---
