---
description: Request body for creating a push dataset
layout: schema
name: CreateDatasetRequest
properties_list:
- description: The display name of the dataset
  name: name
  type: string
- description: The dataset mode
  name: defaultMode
  type: string
- description: The tables within the dataset
  name: tables
  type: array
- description: Relationships between tables
  name: relationships
  type: array
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-create-dataset-request-schema.json
slug: power-bi-rest-create-dataset-request
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: CreateDatasetRequest
---
