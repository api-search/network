---
description: ExtraService schema
layout: schema
name: ExtraService
properties_list:
- description: extra service code, which can take following values code | name ------ | ---------------------------- DSL | Driver language specified EWT | Extra waiting time MAG | Meet & Greet FLM | Flight monitorin
  name: code
  type: string
- description: extra service identifier
  name: itemId
  type: string
- description: extra service description
  name: description
  type: string
- description: extra service time metric type
  name: metricType
  type: string
- description: extra service metric value
  name: metricValue
  type: string
- description: ''
  name: quotation
  type: object
- description: ''
  name: converted
  type: object
- description: true if extra service is available for booking
  name: isBookable
  type: boolean
- description: true if tax included in extra service price
  name: taxIncluded
  type: boolean
- description: true if extra service price is included in total transfer amount
  name: includedInTotal
  type: boolean
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-extra-service-schema.json
slug: transfer-booking-extra-service
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: ExtraService
---
