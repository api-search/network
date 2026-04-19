---
description: A meter definition that specifies how usage events are tracked and aggregated
layout: schema
name: MeterDefinition
properties_list:
- description: Unique API name for the meter
  name: meterApiName
  type: string
- description: Human-readable display name for the meter
  name: displayName
  type: string
- description: Label identifier for the meter
  name: label
  type: string
- description: Aggregation type for the meter
  name: type
  type: string
- description: Creation timestamp in Unix milliseconds
  name: meterTimeInMillis
  type: integer
- description: List of dimension names for this meter
  name: dimensions
  type: array
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/metering-meter-definition-schema.json
slug: metering-meter-definition
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: MeterDefinition
---
