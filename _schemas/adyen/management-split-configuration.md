---
description: SplitConfiguration schema from Adyen API
layout: schema
name: SplitConfiguration
properties_list:
- description: Your description for the split configuration.
  name: description
  type: string
- description: Array of rules that define the split configuration behavior.
  name: rules
  type: array
- description: Unique identifier of the split configuration.
  name: splitConfigurationId
  type: string
- description: List of stores to which the split configuration applies.
  name: stores
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-split-configuration-schema.json
slug: management-split-configuration
tags:
- Payments
- Financial Services
- Fintech
title: SplitConfiguration
---
