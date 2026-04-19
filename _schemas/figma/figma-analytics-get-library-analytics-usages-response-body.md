---
description: ''
layout: schema
name: GetLibraryAnalyticsUsagesResponseBody
properties_list:
- description: An array of analytics data when breaking down usage by component.
  name: components
  type: array
- description: An array of analytics data when breaking down usage by file.
  name: files
  type: array
- description: Whether there is a next page of data that can be fetched.
  name: nextPage
  type: boolean
- description: The cursor to use to fetch the next page of data. Not present if nextPage is false.
  name: cursor
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-analytics-get-library-analytics-usages-response-body-schema.json
slug: figma-analytics-get-library-analytics-usages-response-body
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: GetLibraryAnalyticsUsagesResponseBody
---
