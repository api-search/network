---
description: A relationship between two tables in a dataset
layout: schema
name: Relationship
properties_list:
- description: The name of the relationship
  name: name
  type: string
- description: The source table name
  name: fromTable
  type: string
- description: The source column name
  name: fromColumn
  type: string
- description: The target table name
  name: toTable
  type: string
- description: The target column name
  name: toColumn
  type: string
- description: The cross-filtering direction
  name: crossFilteringBehavior
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-relationship-schema.json
slug: power-bi-rest-relationship
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Relationship
---
