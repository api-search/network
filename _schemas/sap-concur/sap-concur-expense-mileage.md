---
description: Mileage-specific data for distance-based expenses
layout: schema
name: Mileage
properties_list:
- description: Total distance traveled
  name: totalDistance
  type: integer
- description: The identifier of the vehicle used
  name: vehicleId
  type: string
- description: Starting odometer reading
  name: odometerStart
  type: integer
- description: Ending odometer reading
  name: odometerEnd
  type: integer
- description: Number of passengers
  name: passengerCount
  type: integer
- description: Distance attributed to personal use
  name: personalDistance
  type: integer
- description: Whether the higher mileage rate applies
  name: isMarkedAsHigherRate
  type: boolean
- description: The identifier of the route taken
  name: routeId
  type: string
- description: Whether equipment was transported
  name: hasMachinery
  type: boolean
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-mileage-schema.json
slug: sap-concur-expense-mileage
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: Mileage
---
