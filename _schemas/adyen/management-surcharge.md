---
description: Surcharge schema from Adyen API
layout: schema
name: Surcharge
properties_list:
- description: Show the surcharge details on the terminal, so the shopper can confirm.
  name: askConfirmation
  type: boolean
- description: Surcharge fees or percentages for specific payment methods, funding sources (credit or debit), and currencies.
  name: configurations
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-surcharge-schema.json
slug: management-surcharge
tags:
- Payments
- Financial Services
- Fintech
title: Surcharge
---
