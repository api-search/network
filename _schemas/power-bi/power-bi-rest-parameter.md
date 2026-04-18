---
description: A parameter in a dataset
layout: schema
name: Parameter
properties_list:
- description: The parameter name
  name: name
  type: string
- description: The data type of the parameter
  name: type
  type: string
- description: The current value of the parameter
  name: currentValue
  type: string
- description: Whether the parameter is required
  name: isRequired
  type: boolean
- description: Suggested values for the parameter
  name: suggestedValues
  type: array
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-parameter-schema.json
slug: power-bi-rest-parameter
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Parameter
---
