---
description: Request body for creating a data quality rule
layout: schema
name: CreateDataQualityRuleRequest
properties_list:
- description: Rule name
  name: name
  type: string
- description: Type of data quality check
  name: type
  type: string
- description: Dataset identifier to apply the rule to
  name: datasetId
  type: string
- description: Column to monitor
  name: columnName
  type: string
- description: Alert threshold as percentage (0-100)
  name: threshold
  type: number
- description: Severity of alerts triggered by this rule
  name: severity
  type: string
provider_name: Acceldata
provider_slug: acceldata
schema_file: json-schema/adoc-api-create-data-quality-rule-request-schema.json
slug: adoc-api-create-data-quality-rule-request
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
title: CreateDataQualityRuleRequest
---
