---
description: Flight notification message contract
layout: schema
name: FlightNotificationItemContract
properties_list:
- description: Human-readable summary of the flight status update
  name: notificationSummary
  type: string
- description: Human-readable remark to the flight status update
  name: notificationRemark
  type: string
- description: ''
  name: greatCircleDistance
  type: object
- description: ''
  name: departure
  type: object
- description: ''
  name: arrival
  type: object
- description: ''
  name: flightPlan
  type: object
- description: Time (UTC) of the latest update of flight information (excluding Location)
  name: lastUpdatedUtc
  type: string
- description: Flight Number
  name: number
  type: string
- description: ATC call-sign of the flight
  name: callSign
  type: string
- description: ''
  name: status
  type: object
- description: ''
  name: codeshareStatus
  type: object
- description: Is cargo flight
  name: isCargo
  type: boolean
- description: ''
  name: aircraft
  type: object
- description: ''
  name: airline
  type: object
- description: ''
  name: location
  type: object
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-notification-item-contract-schema.json
slug: aerodatabox-flight-notification-item-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightNotificationItemContract
---
