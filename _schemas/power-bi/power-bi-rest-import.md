---
description: An import operation
layout: schema
name: Import
properties_list:
- description: The unique identifier of the import
  name: id
  type: string
- description: The display name of the import
  name: name
  type: string
- description: The state of the import
  name: importState
  type: string
- description: When the import was created
  name: createdDateTime
  type: string
- description: When the import was last updated
  name: updatedDateTime
  type: string
- description: Reports created by this import
  name: reports
  type: array
- description: Datasets created by this import
  name: datasets
  type: array
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-import-schema.json
slug: power-bi-rest-import
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Import
---
