---
description: A calculated metric definition
layout: schema
name: CalculatedMetric
properties_list:
- description: Unique calculated metric identifier
  name: id
  type: string
- description: Display name
  name: name
  type: string
- description: Description of what the metric measures
  name: description
  type: string
- description: The report suite this calculated metric is based on
  name: rsid
  type: string
- description: The owner of an Analytics component
  name: owner
  type: object
- description: The formula definition for this calculated metric
  name: definition
  type: object
- description: Last modification timestamp
  name: modified
  type: string
- description: The metric type
  name: type
  type: string
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-calculated-metric-schema.json
slug: adobe-analytics-calculated-metric
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: CalculatedMetric
---
