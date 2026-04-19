---
description: the deposit/prepay policy information applicable to the offer. It includes accepted payments, deadline and the amount due
layout: schema
name: HotelProduct_DepositPolicy
properties_list:
- description: Deposit-Prepay amount
  name: amount
  type: string
- description: 'The date and time of the deadline in ISO 8601[https://www.w3.org/TR/NOTE-datetime]. Example: 2010-08-14T13:00:00 Please note that this value is expressed in the hotels local time zone'
  name: deadline
  type: string
- description: ''
  name: description
  type: object
- description: ''
  name: acceptedPayments
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-hotel-product_-deposit-policy-schema.json
slug: hotel-booking-hotel-product_-deposit-policy
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: HotelProduct_DepositPolicy
---
