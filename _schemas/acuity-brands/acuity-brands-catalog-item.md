---
description: Acuity Brands product catalog item
layout: schema
name: CatalogItem
properties_list:
- description: Product number/SKU
  name: productNumber
  type: string
- description: Product name
  name: name
  type: string
- description: Brand name
  name: brand
  type: string
- description: Product category
  name: category
  type: string
- description: Product subcategory
  name: subcategory
  type: string
- description: Full product description
  name: description
  type: string
- description: Technical specifications
  name: specifications
  type: object
- description: Product certifications
  name: certifications
  type: array
- description: List price in USD
  name: listPrice
  type: number
- description: UPC code
  name: upc
  type: string
- description: Primary product image URL
  name: imageUrl
  type: string
- description: Product data sheet URL
  name: dataSheetUrl
  type: string
provider_name: acuity-brands
provider_slug: acuity-brands
schema_file: json-schema/acuity-brands-catalog-item-schema.json
slug: acuity-brands-catalog-item
tags: []
title: CatalogItem
---
