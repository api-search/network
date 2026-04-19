---
description: A group of detected rich result items of a single type.
layout: schema
name: DetectedItems
properties_list:
- description: The rich result type detected (e.g., Product, Recipe, FAQ, BreadcrumbList, Article).
  name: richResultType
  type: string
- description: The individual detected items of this type.
  name: items
  type: array
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-detected-items-schema.json
slug: google-search-console-detected-items
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: DetectedItems
---
