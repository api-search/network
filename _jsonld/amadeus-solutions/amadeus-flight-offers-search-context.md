---
class_count: 32
classes:
- OriginalFlightEndPoint
- OriginalFlightStop
- Error_400
- OperatingFlight
- ExtendedPricingOptions
- Collection_Meta
- DateTimeType
- GetFlightOffersQuery
- SearchCriteria
- BaggageAllowance
- ConnectionRestriction
- Issue
- FlightOffer
- AllotmentDetails
- FlightFilters
- LocationValue
- CarrierRestrictions
- CabinRestriction
- Co2Emission
- Collection_Meta_Link
- Price
- Extended_Price
- AircraftEquipment
- OriginDestinationLight
- Tax
- Extended_PricingOptions
- Dictionaries
- FlightSegment
- ChargeableSeat
- Fee
- TravelerInfo
- Error_500
context_file: json-ld/amadeus-flight-offers-search-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/json-ld/amadeus-flight-offers-search-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Flight Offers Search from Amadeus Solutions.
layout: jsonld
name: Amadeus Flight Offers Search Context
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
  name: iataCode
  type: string
- container: ''
  name: terminal
  type: string
- container: ''
  name: duration
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: carrierCode
  type: string
- container: ''
  name: includedCheckedBagsOnly
  type: boolean
- container: ''
  name: refundableFare
  type: boolean
- container: ''
  name: noRestrictionFare
  type: boolean
- container: ''
  name: noPenaltyFare
  type: boolean
- container: ''
  name: count
  type: integer
- container: set
  name: oneWayCombinations
  type: string
- container: ''
  name: date
  type: date
- container: ''
  name: time
  type: string
- container: ''
  name: currencyCode
  type: string
- container: set
  name: originDestinations
  type: string
- container: set
  name: travelers
  type: string
- container: set
  name: sources
  type: string
- container: ''
  name: searchCriteria
  type: string
- container: ''
  name: excludeAllotments
  type: boolean
- container: ''
  name: addOneWayOffers
  type: boolean
- container: ''
  name: maxFlightOffers
  type: decimal
- container: ''
  name: maxPrice
  type: integer
- container: ''
  name: allowAlternativeFareOptions
  type: boolean
- container: ''
  name: oneFlightOfferPerDay
  type: boolean
- container: ''
  name: additionalInformation
  type: string
- container: ''
  name: pricingOptions
  type: string
- container: ''
  name: flightFilters
  type: string
- container: ''
  name: quantity
  type: integer
- container: ''
  name: weight
  type: integer
- container: ''
  name: weightUnit
  type: string
- container: ''
  name: maxNumberOfConnections
  type: decimal
- container: ''
  name: nonStopPreferred
  type: boolean
- container: ''
  name: airportChangeAllowed
  type: boolean
- container: ''
  name: technicalStopsAllowed
  type: boolean
- container: ''
  name: status
  type: integer
- container: ''
  name: code
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
  name: type
  type: string
- container: ''
  name: id
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
- container: set
  name: validatingAirlineCodes
  type: string
- container: set
  name: travelerPricings
  type: string
- container: ''
  name: tourName
  type: string
- container: ''
  name: tourReference
  type: string
- container: ''
  name: crossBorderAllowed
  type: boolean
- container: ''
  name: moreOvernightsAllowed
  type: boolean
- container: ''
  name: returnToDepartureAirport
  type: boolean
- container: ''
  name: railSegmentAllowed
  type: boolean
- container: ''
  name: busSegmentAllowed
  type: boolean
- container: ''
  name: maxFlightTime
  type: decimal
- container: ''
  name: carrierRestrictions
  type: string
- container: set
  name: cabinRestrictions
  type: string
- container: ''
  name: connectionRestriction
  type: string
- container: ''
  name: cityCode
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: blacklistedInEUAllowed
  type: boolean
- container: set
  name: excludedCarrierCodes
  type: string
- container: set
  name: includedCarrierCodes
  type: string
- container: ''
  name: cabin
  type: string
- container: set
  name: originDestinationIds
  type: string
- container: ''
  name: links
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
  name: originLocationCode
  type: string
- container: ''
  name: destinationLocationCode
  type: string
- container: set
  name: includedConnectionPoints
  type: string
- container: set
  name: excludedConnectionPoints
  type: string
- container: ''
  name: amount
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
  name: departure
  type: string
- container: ''
  name: arrival
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: operating
  type: string
- container: set
  name: stops
  type: string
- container: ''
  name: travelerType
  type: string
- container: ''
  name: associatedAdultId
  type: string
property_count: 94
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
slug: amadeus-flight-offers-search-context
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
