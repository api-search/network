---
description: InputDetail schema from Adyen API
layout: schema
name: InputDetail
properties_list:
- description: Configuration parameters for the required input.
  name: configuration
  type: object
- description: Input details can also be provided recursively.
  name: details
  type: array
- description: Input details can also be provided recursively (deprecated).
  name: inputDetails
  type: array
- description: In case of a select, the URL from which to query the items.
  name: itemSearchUrl
  type: string
- description: In case of a select, the items to choose from.
  name: items
  type: array
- description: The value to provide in the result.
  name: key
  type: string
- description: True if this input value is optional.
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
schema_file: json-schema/checkout-input-detail-schema.json
slug: checkout-input-detail
tags:
- Payments
- Financial Services
- Fintech
title: InputDetail
---
