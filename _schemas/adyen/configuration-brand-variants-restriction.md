---
description: BrandVariantsRestriction schema from Adyen API
layout: schema
name: BrandVariantsRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: 'List of card brand variants. Possible values: - **mc**, **mccredit**, **mccommercialcredit_b2b**, **mcdebit**, **mcbusinessdebit**, **mcbusinessworlddebit**, **mcprepaid**, **mcmaestro** - **visa**, *'
  name: value
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-brand-variants-restriction-schema.json
slug: configuration-brand-variants-restriction
tags:
- Payments
- Financial Services
- Fintech
title: BrandVariantsRestriction
---
