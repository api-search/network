---
description: cancellation rule information
layout: schema
name: CancellationRule
properties_list:
- description: description of cancellation rule
  name: ruleDescription
  type: string
- description: type of fee - percentage of total amount (PERCENTAGE) or fixed amount (VALUE)
  name: feeType
  type: string
- description: value of the fee, e.g. "100" or "12.50"
  name: feeValue
  type: string
- description: currency code of the fee in [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. USD, EUR
  name: currencyCode
  type: string
- description: type of metric
  name: metricType
  type: string
- description: metric min value
  name: metricMin
  type: string
- description: metric max value
  name: metricMax
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-cancellation-rule-schema.json
slug: transfer-booking-cancellation-rule
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: CancellationRule
---
