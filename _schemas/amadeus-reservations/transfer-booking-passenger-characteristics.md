---
description: PassengerCharacteristics schema
layout: schema
name: PassengerCharacteristics
properties_list:
- description: Passenger type codes e.g. CHD , ADT. CHD is for child and ADT for Adult.
  name: passengerTypeCode
  type: string
- description: Age of the Passenger (Mandatory if typeCode= “CHD”)
  name: age
  type: integer
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-passenger-characteristics-schema.json
slug: transfer-booking-passenger-characteristics
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: PassengerCharacteristics
---
