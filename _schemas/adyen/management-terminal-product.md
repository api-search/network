---
description: TerminalProduct schema from Adyen API
layout: schema
name: TerminalProduct
properties_list:
- description: Information about items included and integration options.
  name: description
  type: string
- description: The unique identifier of the product.
  name: id
  type: string
- description: A list of parts included in the terminal package.
  name: itemsIncluded
  type: array
- description: The descriptive name of the product.
  name: name
  type: string
- description: The price of the product.
  name: price
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-terminal-product-schema.json
slug: management-terminal-product
tags:
- Payments
- Financial Services
- Fintech
title: TerminalProduct
---
