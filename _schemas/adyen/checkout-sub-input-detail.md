---
description: SubInputDetail schema from Adyen API
layout: schema
name: SubInputDetail
properties_list:
- description: Configuration parameters for the required input.
  name: configuration
  type: object
- description: In case of a select, the items to choose from.
  name: items
  type: array
- description: The value to provide in the result.
  name: key
  type: string
- description: True if this input is optional to provide.
  name: optional
  type: boolean
- description: The type of the required input.
  name: type
  type: string
- description: The value can be pre-filled, if available.
  name: value
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-sub-input-detail-schema.json
slug: checkout-sub-input-detail
tags:
- Payments
- Financial Services
- Fintech
title: SubInputDetail
---
