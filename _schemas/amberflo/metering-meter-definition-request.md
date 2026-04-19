---
description: Request body for creating a meter definition
layout: schema
name: MeterDefinitionRequest
properties_list:
- description: Unique API name for the meter
  name: meterApiName
  type: string
- description: Human-readable display name
  name: displayName
  type: string
- description: Aggregation type for the meter
  name: type
  type: string
- description: Dimension names for this meter
  name: dimensions
  type: array
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/metering-meter-definition-request-schema.json
slug: metering-meter-definition-request
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: MeterDefinitionRequest
---
