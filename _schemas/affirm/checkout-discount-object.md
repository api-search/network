---
description: Represents a discount applied to the checkout.
layout: schema
name: DiscountObject
properties_list:
- description: The discount amount in cents.
  name: discount_amount
  type: integer
- description: Customer-facing name or description of the discount.
  name: discount_display_name
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/checkout-discount-object-schema.json
slug: checkout-discount-object
tags: []
title: DiscountObject
---
