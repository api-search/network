---
description: A registered dataset in Acceldata
layout: schema
name: Dataset
properties_list:
- description: Unique dataset identifier
  name: id
  type: string
- description: Dataset name (table or file name)
  name: name
  type: string
- description: Data source platform
  name: source
  type: string
- description: Database name
  name: database
  type: string
- description: Schema name
  name: schema
  type: string
- description: Overall data quality score (0-100)
  name: qualityScore
  type: number
- description: Last time the dataset was scanned
  name: lastScanned
  type: string
- description: Number of rows in the dataset
  name: rowCount
  type: integer
- description: Number of columns in the dataset
  name: columnCount
  type: integer
provider_name: Acceldata
provider_slug: acceldata
schema_file: json-schema/adoc-api-dataset-schema.json
slug: adoc-api-dataset
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
title: Dataset
---
