---
description: phone information
layout: schema
name: Phone
properties_list:
- description: ''
  name: deviceType
  type: object
- description: Country calling code of the phone number, as defined by the International Communication Union. Examples - "1" for US, "371" for Latvia.
  name: countryCallingCode
  type: string
- description: Phone number. Composed of digits only. The number of digits depends on the country.
  name: number
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-order-management-phone-schema.json
slug: flight-order-management-phone
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Phone
---
