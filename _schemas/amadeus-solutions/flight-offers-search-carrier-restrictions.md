---
description: Restriction towards carriers.
layout: schema
name: CarrierRestrictions
properties_list:
- description: 'This flag enable/disable filtering of blacklisted airline by EU. The list of the banned airlines is published in the Official Journal of the European Union, where they are included as annexes A and B '
  name: blacklistedInEUAllowed
  type: boolean
- description: This option ensures that the system will only consider these airlines.
  name: excludedCarrierCodes
  type: array
- description: This option ensures that the system will only consider these airlines.
  name: includedCarrierCodes
  type: array
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/flight-offers-search-carrier-restrictions-schema.json
slug: flight-offers-search-carrier-restrictions
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: CarrierRestrictions
---
