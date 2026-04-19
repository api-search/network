---
description: An industrial gas product offered by Air Products
layout: schema
name: IndustrialGasProduct
properties_list:
- description: Unique product identifier
  name: product_id
  type: string
- description: Product name
  name: name
  type: string
- description: Chemical formula
  name: chemical_formula
  type: string
- description: Purity grade classification
  name: purity_grade
  type: string
- description: Purity percentage
  name: purity_percent
  type: number
- description: 'Physical form: gas, liquid, dissolved'
  name: form
  type: string
- description: Industries and applications served
  name: applications
  type: array
- description: DOT hazard class
  name: safety_class
  type: string
provider_name: Air Products and Chemicals
provider_slug: air-products-and-chemicals
schema_file: json-schema/airproducts-industrial-gas-product-schema.json
slug: airproducts-industrial-gas-product
tags:
- Industrial Gases
- Chemicals
- Energy
- Manufacturing
- Hydrogen
- Enterprise
title: IndustrialGasProduct
---
