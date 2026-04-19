---
description: ticketing agreement
layout: schema
name: TicketingAgreement
properties_list:
- description: ''
  name: option
  type: object
- description: Delay before applying automatic process if no issuance in days
  name: delay
  type: string
- description: Exact date to apply automatic process if no issuance. YYYY-MM-DD format, e.g. 2019-06-07
  name: dateTime
  type: string
- description: Ids of the impacted segments
  name: segmentIds
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-order-management-ticketing-agreement-schema.json
slug: flight-order-management-ticketing-agreement
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: TicketingAgreement
---
