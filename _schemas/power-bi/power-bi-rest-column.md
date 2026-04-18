---
description: A column in a dataset table
layout: schema
name: Column
properties_list:
- description: The column name
  name: name
  type: string
- description: The data type of the column
  name: dataType
  type: string
- description: Optional format string for the column
  name: formatString
  type: string
- description: Name of the column to sort by
  name: sortByColumn
  type: string
- description: Whether the column is hidden in reports
  name: isHidden
  type: boolean
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-column-schema.json
slug: power-bi-rest-column
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Column
---
