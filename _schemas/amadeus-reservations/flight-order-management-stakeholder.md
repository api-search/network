---
description: stakeholder definition
layout: schema
name: Stakeholder
properties_list:
- description: item identifier
  name: id
  type: string
- description: The date of birth in ISO 8601 format (yyyy-mm-dd)
  name: dateOfBirth
  type: string
- description: ''
  name: gender
  type: object
- description: ''
  name: name
  type: object
- description: Advanced Passenger Information - regulatory identity documents - SSR DOCS & DOCO elements
  name: documents
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-order-management-stakeholder-schema.json
slug: flight-order-management-stakeholder
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Stakeholder
---
