---
description: AdditionalCommission schema from Adyen API
layout: schema
name: AdditionalCommission
properties_list:
- description: Unique identifier of the balance account to which the additional commission is booked.
  name: balanceAccountId
  type: string
- description: A fixed commission fee, in minor units.
  name: fixedAmount
  type: integer
- description: A variable commission fee, in basis points.
  name: variablePercentage
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-additional-commission-schema.json
slug: management-additional-commission
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalCommission
---
