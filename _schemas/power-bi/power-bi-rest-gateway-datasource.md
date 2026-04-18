---
description: A data source on a gateway
layout: schema
name: GatewayDatasource
properties_list:
- description: The unique identifier of the data source
  name: id
  type: string
- description: The gateway this data source belongs to
  name: gatewayId
  type: string
- description: The type of data source
  name: datasourceType
  type: string
- description: JSON string with connection details
  name: connectionDetails
  type: string
- description: The credential type used for authentication
  name: credentialType
  type: string
- description: The display name of the data source
  name: datasourceName
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-gateway-datasource-schema.json
slug: power-bi-rest-gateway-datasource
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: GatewayDatasource
---
