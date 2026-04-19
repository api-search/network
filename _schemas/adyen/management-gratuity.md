---
description: Gratuity schema from Adyen API
layout: schema
name: Gratuity
properties_list:
- description: Indicates whether one of the predefined tipping options is to let the shopper enter a custom tip. If **true**, only three of the other options defined in `predefinedTipEntries` are shown.
  name: allowCustomAmount
  type: boolean
- description: The currency that the tipping settings apply to.
  name: currency
  type: string
- description: 'Tipping options the shopper can choose from if `usePredefinedTipEntries` is **true**. The maximum number of predefined options is four, or three plus the option to enter a custom tip. The options can '
  name: predefinedTipEntries
  type: array
- description: Indicates whether the terminal shows a prompt to enter a tip (**false**), or predefined tipping options to choose from (**true**).
  name: usePredefinedTipEntries
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-gratuity-schema.json
slug: management-gratuity
tags:
- Payments
- Financial Services
- Fintech
title: Gratuity
---
