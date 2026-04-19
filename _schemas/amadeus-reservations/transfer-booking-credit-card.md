---
description: information about payment card
layout: schema
name: CreditCard
properties_list:
- description: card number
  name: number
  type: string
- description: card holder name
  name: holderName
  type: string
- description: card vendor code, e.g VI – VISA, CA – MasterCard, AX – American Express etc
  name: vendorCode
  type: string
- description: card expiry date in format MMYY, e.g. 0237 for February 2037
  name: expiryDate
  type: string
- description: cerification calue number, as indicated on the credit card. Only for query
  name: cvv
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-credit-card-schema.json
slug: transfer-booking-credit-card
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: CreditCard
---
