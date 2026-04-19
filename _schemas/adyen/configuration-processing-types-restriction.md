---
description: ProcessingTypesRestriction schema from Adyen API
layout: schema
name: ProcessingTypesRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: 'List of processing types. Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **recurring**, **token**.'
  name: value
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-processing-types-restriction-schema.json
slug: configuration-processing-types-restriction
tags:
- Payments
- Financial Services
- Fintech
title: ProcessingTypesRestriction
---
