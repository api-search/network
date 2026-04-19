---
description: b2b wallet
layout: schema
name: B2bWallet
properties_list:
- description: card identifier
  name: cardId
  type: string
- description: card usage name
  name: cardUsageName
  type: string
- description: card name
  name: cardFriendlyName
  type: string
- description: ''
  name: reportingData
  type: array
- description: ''
  name: virtualCreditCardDetails
  type: object
- description: Id of the concern flightOffers
  name: flightOfferIds
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-create-orders-b2b-wallet-schema.json
slug: flight-create-orders-b2b-wallet
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: B2bWallet
---
