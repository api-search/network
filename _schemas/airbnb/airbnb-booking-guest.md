---
description: ''
layout: schema
name: BookingGuest
properties_list:
- description: The unique identifier of the guest.
  name: id
  type: string
- description: The first name of the guest.
  name: first_name
  type: string
- description: The last name of the guest.
  name: last_name
  type: string
- description: The phone number of the guest.
  name: phone
  type: string
- description: Whether the guest has completed identity verification.
  name: verified
  type: boolean
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-booking-guest-schema.json
slug: airbnb-booking-guest
tags: []
title: BookingGuest
---
