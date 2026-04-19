---
description: credit card common attribute
layout: schema
name: CreditCardCommon
properties_list:
- description: ''
  name: brand
  type: object
- description: card holder as on the card
  name: holder
  type: string
- description: card number
  name: number
  type: string
- description: credit card expiration date following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (YYYY-MM format, e.g. 2012-08)
  name: expiryDate
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-order-management-credit-card-common-schema.json
slug: flight-order-management-credit-card-common
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: CreditCardCommon
---
