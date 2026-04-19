---
description: ''
layout: schema
name: Reservation
properties_list:
- description: The unique identifier of the reservation.
  name: id
  type: string
- description: The human-readable confirmation code for the reservation.
  name: confirmation_code
  type: string
- description: The current status of the reservation.
  name: status
  type: string
- description: The identifier of the listing that was booked.
  name: listing_id
  type: string
- description: ''
  name: guest
  type: object
- description: The guest check-in date.
  name: check_in
  type: string
- description: The guest check-out date.
  name: check_out
  type: string
- description: The total number of nights in the reservation.
  name: nights
  type: integer
- description: The number of guests included in the reservation.
  name: guests_count
  type: integer
- description: The total price of the reservation in the listing currency.
  name: total_price
  type: number
- description: The ISO 4217 currency code for the reservation pricing.
  name: currency
  type: string
- description: The amount to be paid out to the host after fees.
  name: host_payout
  type: number
- description: The timestamp when the reservation was created.
  name: created_at
  type: string
- description: The timestamp when the reservation was last updated.
  name: updated_at
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-reservation-schema.json
slug: airbnb-reservation
tags: []
title: Reservation
---
