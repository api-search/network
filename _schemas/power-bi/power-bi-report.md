---
description: Schema for a Power BI report resource as returned by the Power BI REST API. A report is a multi-page visual presentation of data from a dataset, with interactive elements for filtering, drilling, and exploring insights.
layout: schema
name: Power BI Report
properties_list:
- description: The unique identifier of the report, assigned by the Power BI service
  name: id
  type: string
- description: The display name of the report
  name: name
  type: string
- description: A text description of the report's purpose and content
  name: description
  type: string
- description: The unique identifier of the dataset that provides data to this report
  name: datasetId
  type: string
- description: The type of report, either an interactive Power BI report or a paginated report
  name: reportType
  type: string
- description: The web URL for viewing the report in the Power BI service
  name: webUrl
  type: string
- description: The URL for embedding the report in third-party applications using the Power BI Embedded service
  name: embedUrl
  type: string
- description: The UTC date and time when the report was first created
  name: createdDateTime
  type: string
- description: The UTC date and time when the report was last modified
  name: modifiedDateTime
  type: string
- description: The display name or email of the user who last modified the report
  name: modifiedBy
  type: string
- description: The display name or email of the user who created the report
  name: createdBy
  type: string
- description: The unique identifier of the workspace containing this report
  name: workspaceId
  type: string
- description: The pages within the report, each containing visualizations and layout
  name: pages
  type: array
- description: The workspace ID of the dataset if it resides in a different workspace from the report
  name: datasetWorkspaceId
  type: string
- description: The app ID if this report is part of a published Power BI app
  name: appId
  type: string
- description: Users who have access to the report and their permissions
  name: users
  type: array
- description: Email subscriptions configured for this report
  name: subscriptions
  type: array
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-report-schema.json
slug: power-bi-report
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Power BI Report
---
