---
description: A data source used by a dataset
layout: schema
name: Datasource
properties_list:
- description: The type of data source (e.g. Sql, AnalysisServices, File)
  name: datasourceType
  type: string
- description: Connection details for the data source
  name: connectionDetails
  type: object
- description: The unique identifier of the data source
  name: datasourceId
  type: string
- description: The gateway identifier if using an on-premises gateway
  name: gatewayId
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-datasource-schema.json
slug: power-bi-rest-datasource
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Datasource
---
