---
description: Data lineage graph for a dataset
layout: schema
name: LineageGraph
properties_list:
- description: Dataset identifier
  name: datasetId
  type: string
- description: Dataset name
  name: datasetName
  type: string
- description: Upstream data sources
  name: upstream
  type: array
- description: Downstream data consumers
  name: downstream
  type: array
provider_name: Acceldata
provider_slug: acceldata
schema_file: json-schema/adoc-api-lineage-graph-schema.json
slug: adoc-api-lineage-graph
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
title: LineageGraph
---
