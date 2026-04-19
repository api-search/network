---
description: MccsRestriction schema from Adyen API
layout: schema
name: MccsRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: List of merchant category codes (MCCs).
  name: value
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-mccs-restriction-schema.json
slug: configuration-mccs-restriction
tags:
- Payments
- Financial Services
- Fintech
title: MccsRestriction
---
