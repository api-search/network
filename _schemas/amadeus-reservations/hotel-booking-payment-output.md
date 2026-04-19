---
description: Model with the hotel payment information
layout: schema
name: PaymentOutput
properties_list:
- description: Agency IATA/ARC Number used to Guarantee the booking
  name: iataTravelAgency
  type: object
- description: To be used when the booking is paid with to a virtual credit card generated through an external provider like Conferma. The Billback account number is mandatory. The rest of the information is not man
  name: billBack
  type: object
- description: 'Indicates the method of payment. - CREDIT_CARD : It allows payment through a credit card. It is expected to provide the credit card information in the creditCard section. - AGENCY_ACCOUNT (CREDIT LINE'
  name: method
  type: string
- description: To perform a booking with B2B wallet, no extra information is needed in input. Information on the virtal credit card generated, is provided in this section in reply.
  name: b2bWallet
  type: object
- description: Credit card information.
  name: paymentCard
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-payment-output-schema.json
slug: hotel-booking-payment-output
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: PaymentOutput
---
