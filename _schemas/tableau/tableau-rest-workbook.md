---
description: ''
layout: schema
name: Workbook
properties_list:
- description: The unique identifier for the workbook.
  name: id
  type: string
- description: The name of the workbook.
  name: name
  type: string
- description: A description of the workbook.
  name: description
  type: string
- description: The URL name of the workbook, used in URLs to access the workbook.
  name: contentUrl
  type: string
- description: The full URL to the workbook on the server.
  name: webpageUrl
  type: string
- description: Whether the workbook shows views as tabs.
  name: showTabs
  type: boolean
- description: The size of the workbook in bytes.
  name: size
  type: integer
- description: The date and time the workbook was created.
  name: createdAt
  type: string
- description: The date and time the workbook was last updated.
  name: updatedAt
  type: string
- description: Whether extracts in the workbook are encrypted.
  name: encryptExtracts
  type: string
- description: The ID of the default view in the workbook.
  name: defaultViewId
  type: string
- description: ''
  name: project
  type: object
- description: ''
  name: owner
  type: object
- description: ''
  name: tags
  type: object
- description: ''
  name: views
  type: object
- description: ''
  name: usage
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-workbook-schema.json
slug: tableau-rest-workbook
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Workbook
---
