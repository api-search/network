---
description: GeneralRemark schema
layout: schema
name: GeneralRemark
properties_list:
- description: ''
  name: subType
  type: object
- description: remark category
  name: category
  type: string
- description: remark free text
  name: text
  type: string
- description: Id of the concerned traveler
  name: travelerIds
  type: array
- description: Id of the concern flightOffers
  name: flightOfferIds
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-create-orders-general-remark-schema.json
slug: flight-create-orders-general-remark
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: GeneralRemark
---
