---
description: AirTravelDocumentCommon schema
layout: schema
name: AirTravelDocumentCommon
properties_list:
- description: Type of the travel document
  name: documentType
  type: string
- description: Identifier of the travel document prefixed by its owner code [NALC - 3 digits]. Can either be a primary or a conjunctive document number. Necessary for TicketingReference definition.
  name: documentNumber
  type: string
- description: Status of the travel document contained in the fare element
  name: documentStatus
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-create-orders-air-travel-document-common-schema.json
slug: flight-create-orders-air-travel-document-common
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: AirTravelDocumentCommon
---
