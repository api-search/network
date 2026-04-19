---
description: address of the departure location
layout: schema
name: AddressCommon
properties_list:
- description: Address line with street, number, bulding, etc...
  name: line
  type: string
- description: Post office code number
  name: zip
  type: string
- description: Country code (two character standard IATA country code)
  name: countryCode
  type: string
- description: City, town or postal station
  name: cityName
  type: string
- description: State code (two character standard IATA state code)
  name: stateCode
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-address-common-schema.json
slug: transfer-booking-address-common
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: AddressCommon
---
