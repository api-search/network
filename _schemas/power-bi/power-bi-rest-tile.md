---
description: A tile on a Power BI dashboard
layout: schema
name: Tile
properties_list:
- description: The unique identifier of the tile
  name: id
  type: string
- description: The display title of the tile
  name: title
  type: string
- description: The subtitle of the tile
  name: subTitle
  type: string
- description: The embed URL for the tile
  name: embedUrl
  type: string
- description: Additional embed data for the tile
  name: embedData
  type: string
- description: The ID of the report the tile is pinned from
  name: reportId
  type: string
- description: The ID of the dataset used by this tile
  name: datasetId
  type: string
- description: The number of rows the tile spans
  name: rowSpan
  type: integer
- description: The number of columns the tile spans
  name: colSpan
  type: integer
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-tile-schema.json
slug: power-bi-rest-tile
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Tile
---
