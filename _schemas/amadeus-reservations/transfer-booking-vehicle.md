---
description: Vehicle schema
layout: schema
name: Vehicle
properties_list:
- description: vehicle type, which can take following values value | description -------------- | ------------------------ CAR | Car SED | Sedan WGN | Wagon ELC | Electric car VAN | Van or minivan SUV | Sport utilit
  name: code
  type: string
- description: category of the vehicle, which can take following values value | description -------------- | ------------------------ ST | Standard BU | Business FC | First class
  name: category
  type: string
- description: description of the vehicle. Can describe a list of potential vehicles, e.g. VW Polo or similar
  name: description
  type: string
- description: ''
  name: seats
  type: array
- description: ''
  name: baggages
  type: array
- description: URL to vehicle image
  name: imageURL
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-vehicle-schema.json
slug: transfer-booking-vehicle
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Vehicle
---
