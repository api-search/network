---
description: Statistical record of route daily statistics
layout: schema
name: DailyRouteStatRecordContract
properties_list:
- description: ''
  name: destination
  type: object
- description: Daily average of flights per destination
  name: averageDailyFlights
  type: number
- description: Airlines operating on the route
  name: operators
  type: array
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-daily-route-stat-record-contract-schema.json
slug: aerodatabox-daily-route-stat-record-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: DailyRouteStatRecordContract
---
