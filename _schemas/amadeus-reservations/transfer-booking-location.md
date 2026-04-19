---
description: location information
layout: schema
name: Location
properties_list:
- description: date and time specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DDThh:mm:ss format e.g. 2017-11-10T10:00:00 not supported for stopOvers object
  name: dateTime
  type: string
- description: airport code from [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx), e.g. CDG.
  name: locationCode
  type: string
- description: ''
  name: address
  type: object
- description: Place name e.g. Airport Name, Hotel Name etc.
  name: name
  type: string
- description: Google place id only for google address e.g. ChIJL-DOWeBv5kcRfTbh97PimNc.
  name: googlePlaceId
  type: string
- description: UIC code defined by the worldwide railway organization e.g. 8600626
  name: uicCode
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-location-schema.json
slug: transfer-booking-location
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Location
---
