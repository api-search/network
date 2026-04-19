---
description: The Warning Definition
layout: schema
name: Warning
properties_list:
- description: A machine-readable error code from the Canned Messages table, that will enable the API Consumers code to handle this type of error
  name: code
  type: integer
- description: An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized
  name: title
  type: string
- description: An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be
  name: detail
  type: string
- description: The Warning Source Definition
  name: source
  type: object
- description: A link to a web page or file with further documentation to help the API consumer resolve this error
  name: documentation
  type: string
- description: ''
  name: sources
  type: array
- description: Indicate relationships from one entity to many other entities of any kind (e.g. from one passenger to their flight segments).
  name: relationships
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-warning-schema.json
slug: hotel-booking-warning
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Warning
---
