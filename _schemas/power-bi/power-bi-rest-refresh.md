---
description: A dataset refresh operation entry
layout: schema
name: Refresh
properties_list:
- description: The unique identifier of the refresh request
  name: requestId
  type: string
- description: The sequential identifier of the refresh
  name: id
  type: integer
- description: The type of refresh
  name: refreshType
  type: string
- description: The start time of the refresh
  name: startTime
  type: string
- description: The end time of the refresh
  name: endTime
  type: string
- description: The status of the refresh
  name: status
  type: string
- description: JSON-formatted error details if the refresh failed
  name: serviceExceptionJson
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-refresh-schema.json
slug: power-bi-rest-refresh
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Refresh
---
