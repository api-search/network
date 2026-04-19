---
description: OriginDestinationLight schema
layout: schema
name: OriginDestinationLight
properties_list:
- description: ''
  name: id
  type: string
- description: Origin location, such as a city or an airport. Currently, only the locations defined in [IATA](http://www.iata.org/publications/Pages/code-search.aspx) are supported.
  name: originLocationCode
  type: string
- description: Destination location, such as a city or an airport. Currently, only the locations defined in [IATA](http://www.iata.org/publications/Pages/code-search.aspx) are supported.
  name: destinationLocationCode
  type: string
- description: List of included connections points. When an includedViaPoints option is specified, all FlightOffer returned must at least go via this Connecting Point. Currently, only the locations defined in IATA a
  name: includedConnectionPoints
  type: array
- description: List of excluded connections points. Any FlightOffer with these connections points will be present in response. Currently, only the locations defined in IATA are supported. Used only by the AMADEUS pr
  name: excludedConnectionPoints
  type: array
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/flight-offers-search-origin-destination-light-schema.json
slug: flight-offers-search-origin-destination-light
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: OriginDestinationLight
---
