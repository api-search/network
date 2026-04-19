---
description: Payment schema
layout: schema
name: Payment
properties_list:
- description: ''
  name: brand
  type: object
- description: The first 6 digits of the credit card
  name: binNumber
  type: integer
- description: Id of the flightOffers to pay
  name: flightOfferIds
  type: array
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/branded-fares-upsell-payment-schema.json
slug: branded-fares-upsell-payment
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: Payment
---
