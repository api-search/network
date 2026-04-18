---
description: A Tableau workbook containing one or more views (worksheets, dashboards, or stories) that connect to data sources and provide interactive visual analytics.
layout: schema
name: Tableau Workbook
properties_list:
- description: The unique identifier (LUID) for the workbook.
  name: id
  type: string
- description: The name of the workbook as it appears on the server.
  name: name
  type: string
- description: A user-provided description of the workbook.
  name: description
  type:
  - string
  - 'null'
- description: The URL-friendly name of the workbook used in the content URL path. Automatically generated from the workbook name.
  name: contentUrl
  type: string
- description: The full URL to view the workbook in a web browser on Tableau Server or Tableau Cloud.
  name: webpageUrl
  type: string
- description: Whether the workbook displays views as navigable tabs.
  name: showTabs
  type: boolean
- description: The size of the workbook file in bytes.
  name: size
  type: integer
- description: The ISO 8601 timestamp when the workbook was first published to the server.
  name: createdAt
  type: string
- description: The ISO 8601 timestamp when the workbook was last modified or republished.
  name: updatedAt
  type: string
- description: Whether extracts embedded in the workbook are encrypted at rest.
  name: encryptExtracts
  type: string
- description: The ID of the view that is displayed by default when the workbook is opened.
  name: defaultViewId
  type:
  - string
  - 'null'
- description: ''
  name: project
  type: object
- description: ''
  name: owner
  type: object
- description: Tags associated with the workbook for categorization and search.
  name: tags
  type: object
- description: The views (worksheets, dashboards, and stories) contained in the workbook.
  name: views
  type: object
- description: The data connections used by the workbook.
  name: connections
  type: object
- description: ''
  name: usage
  type: object
- description: Configuration for Data Acceleration on the workbook.
  name: dataAccelerationConfig
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-workbook-schema.json
slug: tableau-workbook
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Tableau Workbook
---
