---
description: input parameter to price flight offers element
layout: schema
name: FlightOfferPricingIn
properties_list:
- description: the resource name
  name: type
  type: string
- description: list of flight offer to price
  name: flightOffers
  type: array
- description: payment information for retrieve eventual credit card fees
  name: payments
  type: array
- description: list of travelers
  name: travelers
  type: array
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/flight-offers-price-flight-offer-pricing-in-schema.json
slug: flight-offers-price-flight-offer-pricing-in
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: FlightOfferPricingIn
---
