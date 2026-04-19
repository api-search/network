---
description: ''
layout: schema
name: Booking
properties_list:
- description: The unique identifier of the booking.
  name: id
  type: string
- description: The human-readable confirmation code for the booking.
  name: confirmation_code
  type: string
- description: The current status of the booking.
  name: status
  type: string
- description: The identifier of the booked experience.
  name: experience_id
  type: string
- description: The identifier of the booked schedule entry.
  name: schedule_id
  type: string
- description: ''
  name: guest
  type: object
- description: The number of guests included in the booking.
  name: guests_count
  type: integer
- description: The total price of the booking.
  name: total_price
  type: number
- description: The ISO 4217 currency code for the booking pricing.
  name: currency
  type: string
- description: The amount to be paid out to the host after fees.
  name: host_payout
  type: number
- description: The timestamp when the booking was created.
  name: created_at
  type: string
- description: The timestamp when the booking was last updated.
  name: updated_at
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-booking-schema.json
slug: airbnb-booking
tags: []
title: Booking
---
