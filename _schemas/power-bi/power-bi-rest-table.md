---
description: A table within a Power BI dataset
layout: schema
name: Table
properties_list:
- description: The name of the table
  name: name
  type: string
- description: The columns in the table
  name: columns
  type: array
- description: Rows of data in the table
  name: rows
  type: array
- description: DAX measures defined on the table
  name: measures
  type: array
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-table-schema.json
slug: power-bi-rest-table
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Table
---
