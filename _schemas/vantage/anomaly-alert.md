---
description: An Anomaly Alert that monitors a Cost Report for unexpected cost spikes based on a percentage threshold.
layout: schema
name: Vantage Anomaly Alert
properties_list:
- description: The unique token identifier for the Anomaly Alert.
  name: token
  type: string
- description: The token of the associated Cost Report.
  name: cost_report_token
  type: string
- description: The threshold percentage for anomaly detection.
  name: threshold
  type: number
- description: The date and time the Anomaly Alert was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/anomaly-alert.json
slug: anomaly-alert
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Anomaly Alert
---
