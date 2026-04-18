---
description: Payload for creating or updating a calculated metric
layout: schema
name: CalculatedMetricCreate
properties_list:
- description: Display name
  name: name
  type: string
- description: Description of what the metric measures
  name: description
  type: string
- description: Report suite ID
  name: rsid
  type: string
- description: The formula definition
  name: definition
  type: object
- description: The metric output type
  name: type
  type: string
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-calculated-metric-create-schema.json
slug: adobe-analytics-calculated-metric-create
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: CalculatedMetricCreate
---
