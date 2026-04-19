---
description: Library analytics actions data broken down by component.
layout: schema
name: LibraryAnalyticsActionsByComponent
properties_list:
- description: The date in ISO 8601 format. e.g. 2023-12-13
  name: week
  type: string
- description: Unique, stable id of the component.
  name: componentKey
  type: string
- description: Name of the component.
  name: componentName
  type: string
- description: The number of detach events for this period.
  name: detachments
  type: number
- description: The number of insertion events for this period.
  name: insertions
  type: number
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-analytics-library-analytics-actions-by-component-schema.json
slug: figma-analytics-library-analytics-actions-by-component
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: LibraryAnalyticsActionsByComponent
---
