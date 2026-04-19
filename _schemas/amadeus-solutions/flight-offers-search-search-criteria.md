---
description: SearchCriteria schema
layout: schema
name: SearchCriteria
properties_list:
- description: This option allows to exclude the isAllotment flag associated to a booking class in the search response when it exist.
  name: excludeAllotments
  type: boolean
- description: This option allows activate the one-way combinable feature
  name: addOneWayOffers
  type: boolean
- description: Maximum number of flight offers returned (Max 250)
  name: maxFlightOffers
  type: number
- description: maximum price per traveler. By default, no limit is applied. If specified, the value should be a positive number with no decimals
  name: maxPrice
  type: integer
- description: This option allows to default to a standard fareOption if no offers are found for the selected fareOption.
  name: allowAlternativeFareOptions
  type: boolean
- description: Requests the system to find at least one flight-offer per day, if possible, when a range of dates is specified. Default is false.
  name: oneFlightOfferPerDay
  type: boolean
- description: ''
  name: additionalInformation
  type: object
- description: ''
  name: pricingOptions
  type: object
- description: ''
  name: flightFilters
  type: object
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/flight-offers-search-search-criteria-schema.json
slug: flight-offers-search-search-criteria
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: SearchCriteria
---
