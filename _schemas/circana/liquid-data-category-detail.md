---
description: Detailed category information
layout: schema
name: CategoryDetail
properties_list:
- description: Unique category identifier
  name: category_id
  type: string
- description: Category name
  name: name
  type: string
- description: Category description
  name: description
  type: string
- description: Parent category identifier
  name: parent_id
  type: string
- description: Industry vertical
  name: industry
  type: string
- description: Depth level in the category hierarchy
  name: level
  type: integer
- description: Direct subcategories
  name: subcategories
  type: array
- description: Data availability and coverage information
  name: data_coverage
  type: object
provider_name: Circana
provider_slug: circana
schema_file: json-schema/liquid-data-category-detail-schema.json
slug: liquid-data-category-detail
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
title: CategoryDetail
---
