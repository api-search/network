---
description: MinorUnitsMonetaryValue schema from Adyen API
layout: schema
name: MinorUnitsMonetaryValue
properties_list:
- description: The transaction amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: amount
  type: integer
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes).
  name: currencyCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-minor-units-monetary-value-schema.json
slug: management-minor-units-monetary-value
tags:
- Payments
- Financial Services
- Fintech
title: MinorUnitsMonetaryValue
---
