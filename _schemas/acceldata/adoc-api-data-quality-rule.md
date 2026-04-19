---
description: A data quality monitoring rule
layout: schema
name: DataQualityRule
properties_list:
- description: Unique rule identifier
  name: id
  type: string
- description: Rule name
  name: name
  type: string
- description: Type of data quality check
  name: type
  type: string
- description: Dataset the rule applies to
  name: datasetId
  type: string
- description: Dataset name
  name: datasetName
  type: string
- description: Column the rule monitors
  name: columnName
  type: string
- description: Alert threshold value (percentage or absolute)
  name: threshold
  type: number
- description: Alert severity when rule is violated
  name: severity
  type: string
- description: Rule activation status
  name: status
  type: string
- description: Rule creation timestamp
  name: createdAt
  type: string
provider_name: Acceldata
provider_slug: acceldata
schema_file: json-schema/adoc-api-data-quality-rule-schema.json
slug: adoc-api-data-quality-rule
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
title: DataQualityRule
---
