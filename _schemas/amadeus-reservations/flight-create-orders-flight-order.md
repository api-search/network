---
description: input parameter to create a flight order
layout: schema
name: FlightOrder
properties_list:
- description: the resource name
  name: type
  type: string
- description: unique identifier of the flight order
  name: id
  type: string
- description: office Id where to queue the order
  name: queuingOfficeId
  type: string
- description: office Id where will be transfered the ownership of the order
  name: ownerOfficeId
  type: string
- description: list of associated record
  name: associatedRecords
  type: array
- description: list of flight offer
  name: flightOffers
  type: array
- description: list of travelers
  name: travelers
  type: array
- description: list of global remarks
  name: remarks
  type: object
- description: list of form of payments
  name: formOfPayments
  type: array
- description: ''
  name: ticketingAgreement
  type: object
- description: list of automatic queuing
  name: automatedProcess
  type: array
- description: list of general contact information
  name: contacts
  type: array
- description: list of tickets
  name: tickets
  type: array
- description: list of forms of identifications applicable to travelers by airline
  name: formOfIdentifications
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-create-orders-flight-order-schema.json
slug: flight-create-orders-flight-order
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: FlightOrder
---
