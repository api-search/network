---
description: Travel-specific data for transportation expenses
layout: schema
name: Travel
properties_list:
- description: Trip origin location
  name: startLocation
  type: string
- description: Trip destination location
  name: endLocation
  type: string
- description: Ticket or booking reference number
  name: ticketNumber
  type: string
- description: Hotel check-in date
  name: hotelCheckinDate
  type: string
- description: Hotel check-out date
  name: hotelCheckoutDate
  type: string
- description: Number of car rental days
  name: carRentalDays
  type: integer
- description: Airline cabin class code
  name: airlineServiceClassCode
  type: string
- description: Airline fee type identifier
  name: airlineFeeTypeCode
  type: string
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-travel-schema.json
slug: sap-concur-expense-travel
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: Travel
---
