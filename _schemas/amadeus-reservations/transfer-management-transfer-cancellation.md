---
description: information returned in cancelation response
layout: schema
name: TransferCancellation
properties_list:
- description: transfer identifier - confirmation number from service provider that identifies the ride
  name: confirmNbr
  type: string
- description: status of reservation
  name: reservationStatus
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-management-transfer-cancellation-schema.json
slug: transfer-management-transfer-cancellation
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: TransferCancellation
---
