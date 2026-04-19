---
description: A rule for filtering meter events before ingestion
layout: schema
name: FilteringRule
properties_list:
- description: The meter API name this rule applies to
  name: meterApiName
  type: string
- description: Unique identifier for this filtering rule
  name: ruleId
  type: string
- description: The dimension to filter on
  name: dimensionName
  type: string
- description: Values to include or exclude
  name: dimensionValues
  type: array
- description: Whether to include or exclude matching events
  name: action
  type: string
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/metering-filtering-rule-schema.json
slug: metering-filtering-rule
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: FilteringRule
---
