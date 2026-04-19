---
description: the information that are found on an ID document
layout: schema
name: Document
properties_list:
- description: The document number (shown on the document) . E.g. QFU514563221J
  name: number
  type: string
- description: Date at which the document has been issued.
  name: issuanceDate
  type: string
- description: Date after which the document is not valid anymore.
  name: expiryDate
  type: string
- description: '[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country that issued the document'
  name: issuanceCountry
  type: string
- description: A more precise information concerning the place where the document has been issued, when available. It may be a country, a state, a city or any other type of location. e.g. New-York
  name: issuanceLocation
  type: string
- description: '[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the nationality appearing on the document'
  name: nationality
  type: string
- description: Birth place as indicated on the document
  name: birthPlace
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-order-management-document-schema.json
slug: flight-order-management-document
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Document
---
