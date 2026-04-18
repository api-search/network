---
description: A stock content category
layout: schema
name: Category
properties_list:
- description: Unique category identifier
  name: id
  type: integer
- description: Localized category name
  name: name
  type: string
- description: URL to browse this category on the Adobe Stock website
  name: link
  type: string
- description: Child subcategories (present in category tree responses)
  name: children
  type: array
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-stock-category-schema.json
slug: adobe-creative-suite-stock-category
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: Category
---
