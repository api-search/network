---
description: A DAX measure defined on a table
layout: schema
name: Measure
properties_list:
- description: The name of the measure
  name: name
  type: string
- description: The DAX expression for the measure
  name: expression
  type: string
- description: Optional format string
  name: formatString
  type: string
- description: Whether the measure is hidden in reports
  name: isHidden
  type: boolean
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-measure-schema.json
slug: power-bi-rest-measure
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Measure
---
