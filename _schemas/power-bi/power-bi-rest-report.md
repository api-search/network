---
description: A Power BI report
layout: schema
name: Report
properties_list:
- description: The unique identifier of the report
  name: id
  type: string
- description: The display name of the report
  name: name
  type: string
- description: The ID of the dataset associated with this report
  name: datasetId
  type: string
- description: The web URL of the report
  name: webUrl
  type: string
- description: The embed URL for embedding the report in applications
  name: embedUrl
  type: string
- description: The type of the report
  name: reportType
  type: string
- description: The report description
  name: description
  type: string
- description: When the report was created
  name: createdDateTime
  type: string
- description: When the report was last modified
  name: modifiedDateTime
  type: string
- description: The user who last modified the report
  name: modifiedBy
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-report-schema.json
slug: power-bi-rest-report
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Report
---
