---
description: description of the name of a physical person
layout: schema
name: Name
properties_list:
- description: The type of the Name
  name: type
  type: string
- description: First name.
  name: firstName
  type: string
- description: Last name.
  name: lastName
  type: string
- description: Contains all the suffixes and prefixes that can be appended to a name - Mr, Miss, Pr. - E.g. " Mr".
  name: title
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-name-schema.json
slug: transfer-booking-name
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Name
---
