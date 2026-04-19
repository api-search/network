---
description: Model with the hotel payment information
layout: schema
name: PaymentInput
properties_list:
- description: Agency IATA/ARC Number used to Guarantee the booking. If not provided it is taken form the Amadeus Office profile.
  name: iataTravelAgency
  type: object
- description: 'Indicates the method of payment. - CREDIT_CARD : It allows payment through a credit card. It is expected to provide the credit card information in the paymentCard section.'
  name: method
  type: string
- description: 'Credit card information. The full details of a credit card are expected : . credit card holder name (mandatory, maximum 64 chars) . credit card vendor code (mandatory) . credit card number (mandatory)'
  name: paymentCard
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-payment-input-schema.json
slug: hotel-booking-payment-input
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: PaymentInput
---
