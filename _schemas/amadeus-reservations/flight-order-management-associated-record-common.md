---
description: describes the relation between the current reservation and another one
layout: schema
name: AssociatedRecordCommon
properties_list:
- description: Record locator [Amadeus or OA] with which the current reservation is related. In case of a codeshare relation, it enables to identify the operating PNR.
  name: reference
  type: string
- description: Creation date of the referenced reservation. Date and time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-ddThh:mm:ss.sss format, e.g. 2019-07-09T12:30:00.000
  name: creationDate
  type: string
- description: Designates the system which has originated the referenced reservation.
  name: originSystemCode
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-order-management-associated-record-common-schema.json
slug: flight-order-management-associated-record-common
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: AssociatedRecordCommon
---
