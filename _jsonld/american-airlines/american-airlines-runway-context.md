---
class_count: 5
classes:
- FlightStatus
- Flight
- FlightList
- BookingRequest
- Booking
context_file: json-ld/american-airlines-runway-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/american-airlines/refs/heads/main/json-ld/american-airlines-runway-context.jsonld
description: JSON-LD context defining the semantic vocabulary for American Airlines Runway from American Airlines.
layout: jsonld
name: American Airlines Runway Context
namespaces:
- prefix: aa
  uri: https://aa.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: flightId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: gate
  type: string
- container: ''
  name: delay
  type: integer
- container: ''
  name: id
  type: string
- container: ''
  name: flightNumber
  type: string
- container: ''
  name: origin
  type: string
- container: ''
  name: destination
  type: string
- container: ''
  name: departureTime
  type: dateTime
- container: ''
  name: arrivalTime
  type: dateTime
- container: set
  name: flights
  type: string
- container: set
  name: passengers
  type: string
property_count: 12
provider_name: American Airlines
provider_slug: american-airlines
slug: american-airlines-runway-context
tags:
- Airlines
- Aviation
- Flights
- Travel
- Booking
- Developer Experience
- JSON-LD
- Linked Data
- Semantic Web
---
