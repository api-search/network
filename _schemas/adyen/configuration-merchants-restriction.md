---
description: MerchantsRestriction schema from Adyen API
layout: schema
name: MerchantsRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: List of merchant ID and acquirer ID pairs.
  name: value
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-merchants-restriction-schema.json
slug: configuration-merchants-restriction
tags:
- Payments
- Financial Services
- Fintech
title: MerchantsRestriction
---
