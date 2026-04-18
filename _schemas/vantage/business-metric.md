---
description: A Business Metric that tracks custom business values over time and can be associated with Cost Reports for unit economics.
layout: schema
name: Vantage Business Metric
properties_list:
- description: The unique token identifier for the Business Metric.
  name: token
  type: string
- description: The title of the Business Metric.
  name: title
  type: string
- description: Associated cost reports with metadata.
  name: cost_report_tokens_with_metadata
  type: array
- description: The values of the Business Metric over time.
  name: values
  type: array
- description: The date and time the Business Metric was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/business-metric.json
slug: business-metric
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Business Metric
---
