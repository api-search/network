---
description: A single meter event representing a unit of usage
layout: schema
name: MeterEvent
properties_list:
- description: The API name of the meter to ingest to
  name: meterApiName
  type: string
- description: Unique identifier for the customer
  name: customerId
  type: string
- description: The usage amount for this event
  name: meterValue
  type: number
- description: Event timestamp in Unix time (milliseconds)
  name: meterTimeInMillis
  type: integer
- description: Custom identifier for event deduplication
  name: uniqueId
  type: string
- description: Key-value pairs for event categorization
  name: dimensions
  type: object
- description: Map of meterApiName to meterValue for multi-meter ingestion
  name: values
  type: object
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/metering-meter-event-schema.json
slug: metering-meter-event
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: MeterEvent
---
