---
description: A filter view.
layout: schema
name: FilterView
properties_list:
- description: The ID of the filter view.
  name: filterViewId
  type: integer
- description: The name of the filter view.
  name: title
  type: string
- description: The named range this filter view is backed by, if any.
  name: namedRangeId
  type: string
- description: The sort order per column.
  name: sortSpecs
  type: array
- description: The criteria for showing/hiding values per column.
  name: criteria
  type: object
- description: The filter criteria for showing/hiding values per column.
  name: filterSpecs
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-filter-view-schema.json
slug: google-sheets-filter-view
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: FilterView
---
