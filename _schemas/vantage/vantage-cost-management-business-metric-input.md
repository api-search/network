---
description: ''
layout: schema
name: BusinessMetricInput
properties_list:
- description: The title of the Business Metric.
  name: title
  type: string
- description: The values of the Business Metric.
  name: values
  type: array
- description: Associated cost reports with metadata.
  name: cost_report_tokens_with_metadata
  type: array
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-business-metric-input-schema.json
slug: vantage-cost-management-business-metric-input
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: BusinessMetricInput
---
