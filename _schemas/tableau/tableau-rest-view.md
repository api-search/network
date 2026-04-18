---
description: ''
layout: schema
name: View
properties_list:
- description: The unique identifier for the view.
  name: id
  type: string
- description: The name of the view.
  name: name
  type: string
- description: The URL name of the view.
  name: contentUrl
  type: string
- description: The date and time the view was created.
  name: createdAt
  type: string
- description: The date and time the view was last updated.
  name: updatedAt
  type: string
- description: The URL-friendly name of the view used in the content URL.
  name: viewUrlName
  type: string
- description: The type of sheet (worksheet, dashboard, or story).
  name: sheetType
  type: string
- description: ''
  name: project
  type: object
- description: ''
  name: owner
  type: object
- description: ''
  name: workbook
  type: object
- description: ''
  name: tags
  type: object
- description: ''
  name: usage
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-view-schema.json
slug: tableau-rest-view
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: View
---
