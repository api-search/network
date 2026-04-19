---
class_count: 37
classes:
- LocationValue
- AllotmentDetails
- Price
- Co2Emission
- OriginalFlightEndPoint
- FareRules
- Dictionaries
- CreditCardFee
- OtherServices
- LoyaltyProgram
- FlightOfferPricingIn
- BaseName
- Error_400
- OriginalFlightStop
- EmergencyContact
- Phone
- FlightSegment
- Stakeholder
- Error_500
- TermAndCondition
- ChargeableSeat
- ElementaryPrice
- Document
- Issue
- OperatingFlight
- Extended_Price
- Address
- Discount
- AircraftEquipment
- ContactDictionary
- BaggageAllowance
- FlightOffer
- Tax
- FlightOfferPricingOut
- Fee
- DetailedFareRules
- name
context_file: json-ld/amadeus-flight-offers-price-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/json-ld/amadeus-flight-offers-price-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Flight Offers Price from Amadeus Solutions.
layout: jsonld
name: Amadeus Flight Offers Price Context
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
  name: cityCode
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: tourName
  type: string
- container: ''
  name: tourReference
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
  name: weight
  type: integer
- container: ''
  name: weightUnit
  type: string
- container: ''
  name: cabin
  type: string
- container: ''
  name: iataCode
  type: string
- container: ''
  name: terminal
  type: string
- container: set
  name: rules
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
  name: brand
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: flightOfferId
  type: string
- container: ''
  name: price
  type: string
- container: ''
  name: bookableByTraveler
  type: boolean
- container: ''
  name: bookableByItinerary
  type: boolean
- container: set
  name: segmentIds
  type: string
- container: set
  name: travelerIds
  type: string
- container: ''
  name: programOwner
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: type
  type: string
- container: set
  name: flightOffers
  type: string
- container: set
  name: payments
  type: string
- container: set
  name: travelers
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: middleName
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: duration
  type: string
- container: ''
  name: addresseeName
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: text
  type: string
- container: ''
  name: deviceType
  type: string
- container: ''
  name: countryCallingCode
  type: string
- container: ''
  name: departure
  type: string
- container: ''
  name: arrival
  type: string
- container: ''
  name: carrierCode
  type: string
- container: ''
  name: operating
  type: string
- container: set
  name: stops
  type: string
- container: ''
  name: dateOfBirth
  type: date
- container: ''
  name: gender
  type: string
- container: set
  name: documents
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: circumstances
  type: string
- container: ''
  name: notApplicable
  type: boolean
- container: ''
  name: maxPenaltyAmount
  type: string
- container: set
  name: descriptions
  type: string
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: issuanceDate
  type: date
- container: ''
  name: expiryDate
  type: date
- container: ''
  name: issuanceCountry
  type: string
- container: ''
  name: issuanceLocation
  type: string
- container: ''
  name: nationality
  type: string
- container: ''
  name: birthPlace
  type: string
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
- container: set
  name: lines
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: cityName
  type: string
- container: ''
  name: stateName
  type: string
- container: ''
  name: postalBox
  type: string
- container: ''
  name: subType
  type: string
- container: ''
  name: travelerType
  type: string
- container: ''
  name: cardNumber
  type: string
- container: ''
  name: certificateNumber
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: purpose
  type: string
- container: ''
  name: quantity
  type: integer
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
  name: pricingOptions
  type: string
- container: set
  name: validatingAirlineCodes
  type: string
- container: set
  name: travelerPricings
  type: string
- container: ''
  name: bookingRequirements
  type: string
- container: ''
  name: fareBasis
  type: string
- container: ''
  name: fareNotes
  type: string
- container: ''
  name: segmentId
  type: string
property_count: 98
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
slug: amadeus-flight-offers-price-context
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
