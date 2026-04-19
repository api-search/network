---
description: A filter on a dashboard that allows users to dynamically change query parameters across multiple tiles simultaneously.
layout: schema
name: DashboardFilter
properties_list:
- description: Unique identifier for this filter
  name: id
  type: string
- description: ID of the parent dashboard
  name: dashboard_id
  type: string
- description: Internal name of the filter
  name: name
  type: string
- description: Display title of the filter
  name: title
  type: string
- description: Filter input type
  name: type
  type: string
- description: LookML model name for field_filter type
  name: model
  type: string
- description: LookML explore name for field_filter type
  name: explore
  type: string
- description: LookML dimension for field_filter type
  name: dimension
  type: string
- description: Default filter value
  name: default_value
  type: string
- description: Whether multiple values can be selected
  name: allow_multiple_values
  type: boolean
- description: Whether the filter must have a value
  name: required
  type: boolean
- description: Row position of the filter in the filter bar
  name: row
  type: integer
- description: Other filters this filter listens to for cascading
  name: listens_to_filters
  type: array
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-dashboard-filter-schema.json
slug: looker-dashboard-filter
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: DashboardFilter
---
