---
description: AmountMinMaxRequirement schema from Adyen API
layout: schema
name: AmountMinMaxRequirement
properties_list:
- description: Specifies the eligible amounts for a particular route.
  name: description
  type: string
- description: Maximum amount.
  name: max
  type: integer
- description: Minimum amount.
  name: min
  type: integer
- description: '**amountMinMaxRequirement**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-amount-min-max-requirement-schema.json
slug: configuration-amount-min-max-requirement
tags:
- Payments
- Financial Services
- Fintech
title: AmountMinMaxRequirement
---
