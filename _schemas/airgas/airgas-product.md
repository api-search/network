---
description: An Airgas product including gases, welding equipment, and safety supplies.
layout: schema
name: Product
properties_list:
- description: Airgas product number / SKU.
  name: product_number
  type: string
- description: Product name.
  name: name
  type: string
- description: Product description.
  name: description
  type: string
- description: Product category.
  name: category
  type: string
- description: Type of gas (for gas products).
  name: gas_type
  type: string
- description: Gas purity grade.
  name: grade
  type: string
- description: Cylinder size designation.
  name: cylinder_size
  type: string
- description: Unit of measure for ordering.
  name: unit_of_measure
  type: string
- description: List price per unit.
  name: price
  type: number
- description: Whether the product is available for order.
  name: available
  type: boolean
provider_name: Airgas
provider_slug: airgas
schema_file: json-schema/airgas-product-schema.json
slug: airgas-product
tags:
- Industrial Gases
- Welding
- Safety
- B2B
- Supply Chain
- Manufacturing
- Healthcare
title: Product
---
