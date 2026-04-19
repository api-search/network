---
description: extra equipment information
layout: schema
name: Equipment
properties_list:
- description: extra equipment codes, which can take following values code | name ------ | ------------------------------------- BBS | Baby stroller/Push chair BYC | Bicycle rack CBB | Cargo barrier rack CBF | Cargo
  name: code
  type: string
- description: extra equipment identifier
  name: itemId
  type: string
- description: extra equipment description
  name: description
  type: string
- description: ''
  name: quotation
  type: object
- description: ''
  name: converted
  type: object
- description: true if extra equipment is available for booking
  name: isBookable
  type: boolean
- description: true if tax included in extra equipment price
  name: taxIncluded
  type: boolean
- description: true if extra equipment price is included in total transfer amount
  name: includedInTotal
  type: boolean
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-equipment-schema.json
slug: transfer-booking-equipment
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Equipment
---
