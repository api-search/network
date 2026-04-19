---
description: elementaryPrice
layout: schema
name: ElementaryPrice
properties_list:
- description: Amount of the fare. could be alpha numeric. Ex- 500.20 or 514.13A, 'A'signifies additional collection.
  name: amount
  type: string
- description: Currency type of the fare.
  name: currencyCode
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-create-orders-elementary-price-schema.json
slug: flight-create-orders-elementary-price
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: ElementaryPrice
---
