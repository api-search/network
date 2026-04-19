---
description: BalanceSweepConfigurationsResponse schema from Adyen API
layout: schema
name: BalanceSweepConfigurationsResponse
properties_list:
- description: Indicates whether there are more items on the next page.
  name: hasNext
  type: boolean
- description: Indicates whether there are more items on the previous page.
  name: hasPrevious
  type: boolean
- description: List of sweeps associated with the balance account.
  name: sweeps
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-balance-sweep-configurations-response-schema.json
slug: configuration-balance-sweep-configurations-response
tags:
- Payments
- Financial Services
- Fintech
title: BalanceSweepConfigurationsResponse
---
