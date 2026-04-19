---
description: Delay information about a batch of flights
layout: schema
name: FlightBatchDelayContract
properties_list:
- description: Total number of flights in the the batch (including cancelled)
  name: numTotal
  type: integer
- description: Total number of flights in the batch, which were used to to calculate the delay information (including cancelled). Should equal to or less than `NumTotal`. The closer the value of this property to the
  name: numQualifiedTotal
  type: integer
- description: Total amount of flights in the batch
  name: numCancelled
  type: integer
- description: 'Median delay of flights in the batch (format: [-]hh:mm:ss). Value can be negative (therefore, means early occurence).'
  name: medianDelay
  type: string
- description: Normalized value on scale from 0.0 to 5.0 which corresponds with current amount of delays and cancellations in a given batch of flights (the less - the better).
  name: delayIndex
  type: number
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-batch-delay-contract-schema.json
slug: aerodatabox-flight-batch-delay-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightBatchDelayContract
---
