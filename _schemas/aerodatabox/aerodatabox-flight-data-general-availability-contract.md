---
description: FlightDataGeneralAvailabilityContract schema from AeroDataBox API
layout: schema
name: FlightDataGeneralAvailabilityContract
properties_list:
- description: Date of the oldest flight stored (based on scheduled local times) If not specified, no flight data available
  name: minAvailableLocalDate
  type: string
- description: Date of the most recent flight stored (based on scheduled local times) If not specified, no flight data available
  name: maxAvailableLocalDate
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-data-general-availability-contract-schema.json
slug: aerodatabox-flight-data-general-availability-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightDataGeneralAvailabilityContract
---
