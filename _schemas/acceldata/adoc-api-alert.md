---
description: A data quality or pipeline monitoring alert
layout: schema
name: Alert
properties_list:
- description: Unique alert identifier
  name: id
  type: string
- description: Alert title
  name: title
  type: string
- description: Alert severity level
  name: severity
  type: string
- description: Current alert status
  name: status
  type: string
- description: Data quality rule that triggered this alert
  name: ruleId
  type: string
- description: Dataset associated with the alert
  name: datasetId
  type: string
- description: Dataset name
  name: datasetName
  type: string
- description: Actual metric value that triggered the alert
  name: metricValue
  type: number
- description: Threshold that was exceeded
  name: threshold
  type: number
- description: When the alert was triggered
  name: triggeredAt
  type: string
provider_name: Acceldata
provider_slug: acceldata
schema_file: json-schema/adoc-api-alert-schema.json
slug: adoc-api-alert
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
title: Alert
---
