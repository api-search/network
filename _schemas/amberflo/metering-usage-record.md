---
description: A usage record grouped by dimension values
layout: schema
name: UsageRecord
properties_list:
- description: Group dimension values for this record
  name: groupInfo
  type: object
- description: Time-series usage data points
  name: records
  type: array
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/metering-usage-record-schema.json
slug: metering-usage-record
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: UsageRecord
---
