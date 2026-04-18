---
description: Request body for cloning a report
layout: schema
name: CloneReportRequest
properties_list:
- description: The name for the cloned report
  name: name
  type: string
- description: Optional dataset ID to rebind the cloned report to
  name: targetModelId
  type: string
- description: Optional workspace ID for the cloned report
  name: targetWorkspaceId
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-clone-report-request-schema.json
slug: power-bi-rest-clone-report-request
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: CloneReportRequest
---
