---
consumed_apis:
- merchant-locations
- atm-locations
- places
- track-search
- transaction-api-acquirers
description: Unified workflow for merchants and acquirers to manage merchant/ATM locations, Places data, Track merchant search, and acquirer transaction processing.
layout: capability
name: Mastercard Merchant Services and Locations
operations:
- description: Search for merchant locations
  method: POST
  name: search-merchant-locations
  path: /v1/merchant-locations
- description: Search for ATM locations
  method: POST
  name: search-atm-locations
  path: /v1/atm-locations
- description: Search for merchant places
  method: POST
  name: search-places
  path: /v1/places
- description: Search for merchants in Track
  method: POST
  name: search-track-merchants
  path: /v1/track-merchants
personas: []
provider_name: Mastercard
provider_slug: mastercard
search_terms:
- search for merchant places with location intelligence
- places location intelligence
- submit acquirer transaction
- search merchant locations
- search for merchant locations
- acquirer
- track merchant data
- search atm locations
- search track merchants
- search places
- merchant
- search for merchants in track
- search for mastercard atm locations
- search for mastercard merchant locations
- list atm countries
- locations
- fraud detection
- merchant location search
- open banking
- mastercard
- search for merchants in the mastercard track network
- digital identity
- list countries with mastercard atms
- track
- atm location search
- search for merchant places
- list countries with merchant locations
- payments
- financial services
- credit cards
- search for atm locations
- list merchant countries
- submit a transaction as an acquirer
slug: merchant-services-and-locations
tags:
- Mastercard
- Merchant
- Locations
- Acquirer
- Track
tools:
- description: Search for Mastercard merchant locations
  hints:
    openWorld: true
    readOnly: true
  name: search-merchant-locations
- description: List countries with merchant locations
  hints:
    idempotent: true
    readOnly: true
  name: list-merchant-countries
- description: Search for Mastercard ATM locations
  hints:
    openWorld: true
    readOnly: true
  name: search-atm-locations
- description: List countries with Mastercard ATMs
  hints:
    idempotent: true
    readOnly: true
  name: list-atm-countries
- description: Search for merchant places with location intelligence
  hints:
    openWorld: true
    readOnly: true
  name: search-places
- description: Search for merchants in the Mastercard Track network
  hints:
    readOnly: true
  name: search-track-merchants
- description: Submit a transaction as an acquirer
  hints:
    readOnly: false
  name: submit-acquirer-transaction
---
