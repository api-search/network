---
class_count: 22
classes:
- Co2Emission
- Collection_Meta_Upsell
- Payment
- OperatingFlight
- Price
- AircraftEquipment
- Error_400
- Fee
- Dictionaries
- Tax
- AllotmentDetails
- Extended_Price
- Issue
- OriginalFlightEndPoint
- ChargeableSeat
- BaggageAllowance
- OriginalFlightStop
- LocationValue
- FlightSegment
- FlightOffer
- Error_500
- FlightOfferUpsellIn
context_file: json-ld/amadeus-branded-fares-upsell-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/json-ld/amadeus-branded-fares-upsell-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Branded Fares Upsell from Amadeus Solutions.
layout: jsonld
name: Amadeus Branded Fares Upsell Context
namespaces:
- prefix: amadeus
  uri: https://amadeus.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: weight
  type: integer
- container: ''
  name: weightUnit
  type: string
- container: ''
  name: cabin
  type: string
- container: ''
  name: count
  type: integer
- container: set
  name: oneWayUpselledCombinations
  type: string
- container: ''
  name: brand
  type: string
- container: ''
  name: binNumber
  type: integer
- container: set
  name: flightOfferIds
  type: string
- container: ''
  name: carrierCode
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: total
  type: string
- container: ''
  name: base
  type: string
- container: set
  name: fees
  type: string
- container: set
  name: taxes
  type: string
- container: ''
  name: refundableTaxes
  type: string
- container: ''
  name: code
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: locations
  type: string
- container: ''
  name: aircraft
  type: string
- container: ''
  name: currencies
  type: string
- container: ''
  name: carriers
  type: string
- container: ''
  name: tourName
  type: string
- container: ''
  name: tourReference
  type: string
- container: ''
  name: status
  type: integer
- container: ''
  name: title
  type: string
- container: ''
  name: detail
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: iataCode
  type: string
- container: ''
  name: terminal
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: quantity
  type: integer
- container: ''
  name: duration
  type: string
- container: ''
  name: cityCode
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: departure
  type: string
- container: ''
  name: arrival
  type: string
- container: ''
  name: operating
  type: string
- container: set
  name: stops
  type: string
- container: ''
  name: instantTicketingRequired
  type: boolean
- container: ''
  name: disablePricing
  type: boolean
- container: ''
  name: nonHomogeneous
  type: boolean
- container: ''
  name: oneWay
  type: boolean
- container: ''
  name: paymentCardRequired
  type: boolean
- container: ''
  name: lastTicketingDate
  type: string
- container: ''
  name: lastTicketingDateTime
  type: dateTime
- container: ''
  name: numberOfBookableSeats
  type: decimal
- container: set
  name: itineraries
  type: string
- container: ''
  name: price
  type: string
- container: ''
  name: pricingOptions
  type: string
- container: set
  name: validatingAirlineCodes
  type: string
- container: set
  name: travelerPricings
  type: string
- container: set
  name: flightOffers
  type: string
- container: set
  name: payments
  type: string
property_count: 56
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
slug: amadeus-branded-fares-upsell-context
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
- JSON-LD
- Linked Data
- Semantic Web
---
