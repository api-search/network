---
description: An Airtable view provides a filtered, sorted, and formatted perspective on the records in a table. Views control which fields are visible, how records are ordered, and which records meet the view's filter criteria.
layout: schema
name: Airtable View
properties_list:
- description: The unique identifier for the view. View IDs always start with the 'viw' prefix.
  name: id
  type: string
- description: The display name of the view.
  name: name
  type: string
- description: The type of view, which determines the layout and interaction model.
  name: type
  type: string
- description: If set, this is a personal view visible only to the specified user. Null indicates a shared view.
  name: personalForUserId
  type:
  - string
  - 'null'
- description: The IDs of fields visible in this view, in display order. Only included when explicitly requested via the include parameter.
  name: visibleFieldIds
  type: array
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-view-schema.json
slug: airtable-view
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable View
---
