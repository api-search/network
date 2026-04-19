---
description: DifferentCurrenciesRestriction schema from Adyen API
layout: schema
name: DifferentCurrenciesRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: 'Checks the currency of the payment against the currency of the payment instrument. Possible values: - **true**: The currency of the payment is different from the currency of the payment instrument. - '
  name: value
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-different-currencies-restriction-schema.json
slug: configuration-different-currencies-restriction
tags:
- Payments
- Financial Services
- Fintech
title: DifferentCurrenciesRestriction
---
