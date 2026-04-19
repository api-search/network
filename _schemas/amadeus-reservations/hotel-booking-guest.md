---
description: This modele represent a guest, his name, his loyalty programs, his age when it is a child...
layout: schema
name: Guest
properties_list:
- description: Airline frequent flyer of the guest /!\ In case of creation of a new hotel booking, only the first element of the array will be transmitted to the hotel provier. Please only provider one. In case of r
  name: frequentTraveler
  type: array
- description: Phone number of the guest It is recommanded to use the standard E.123 (https://en.wikipedia.org/wiki/E.123)
  name: phone
  type: string
- description: Email Adress of the guest
  name: email
  type: string
- description: Title/gender of the guest
  name: title
  type: string
- description: First Name (and middle name) of the guest. It is mandatory at create order but not mandatory at booking creation. - Complex pattern '^[A-Za-z \p{Han}\p{Katakana}\p{Hiragana}\p{Hangul}-]*$'
  name: firstName
  type: string
- description: 'Last name of the guest - It is mandatory at create order but not mandatory at booking creation. Complex pattern: ''^[A-Za-z \p{Han}\p{Katakana}\p{Hiragana}\p{Hangul}-]*$'''
  name: lastName
  type: string
- description: if the guest is a child, it is mandatory to provide a child age. Else the system will consider him as an adult
  name: childAge
  type: integer
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-guest-schema.json
slug: hotel-booking-guest
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Guest
---
