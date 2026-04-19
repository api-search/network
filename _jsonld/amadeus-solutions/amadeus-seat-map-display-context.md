---
class_count: 48
classes:
- OperatingFlight
- FlightOffer
- Document
- Collection_Meta
- AircraftCabinAmenities
- BaseName
- LoyaltyProgram
- Error_400
- ElementaryPrice
- LocationValue
- Price
- FlightEndPoint
- SeatmapTravelerPricing
- EmergencyContact
- Address
- Phone
- Link
- FlightSegment
- Coordinates
- Discount
- FareRules
- SeatCharacteristicDictionary
- Deck
- Fee
- Amenity
- Issue
- FlightStop
- TermAndCondition
- QualifiedFreeText
- Error_404
- Tax
- Amenity_Seat
- Stakeholder
- ContactDictionary
- Co2Emission
- AircraftEquipment
- Error_500
- Facility
- Extended_Price
- DeckConfiguration
- Seat
- SeatMap
- Amenity_Media
- FacilityDictionary
- AvailableSeatsCounter
- BaggageAllowance
- name
- description
context_file: json-ld/amadeus-seat-map-display-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/json-ld/amadeus-seat-map-display-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Seat Map Display from Amadeus Solutions.
layout: jsonld
name: Amadeus Seat Map Display Context
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
  name: carrierCode
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: suffix
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: source
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
- container: ''
  name: fareRules
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
  name: count
  type: integer
- container: ''
  name: links
  type: string
- container: ''
  name: power
  type: string
- container: ''
  name: seat
  type: string
- container: ''
  name: wifi
  type: string
- container: set
  name: entertainment
  type: string
- container: ''
  name: food
  type: string
- container: ''
  name: beverage
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
- container: ''
  name: programOwner
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: cityCode
  type: string
- container: ''
  name: countryCode
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
  name: iataCode
  type: string
- container: ''
  name: terminal
  type: string
- container: ''
  name: at
  type: dateTime
- container: ''
  name: travelerId
  type: string
- container: ''
  name: seatAvailabilityStatus
  type: string
- container: ''
  name: addresseeName
  type: string
- container: ''
  name: text
  type: string
- container: ''
  name: category
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
  name: stateCode
  type: string
- container: ''
  name: stateName
  type: string
- container: ''
  name: postalBox
  type: string
- container: ''
  name: deviceType
  type: string
- container: ''
  name: countryCallingCode
  type: string
- container: ''
  name: areaCode
  type: string
- container: ''
  name: extension
  type: string
- container: ''
  name: href
  type: reference
- container: set
  name: methods
  type: string
- container: ''
  name: departure
  type: string
- container: ''
  name: arrival
  type: string
- container: ''
  name: aircraft
  type: string
- container: ''
  name: operating
  type: string
- container: ''
  name: duration
  type: string
- container: set
  name: stops
  type: string
- container: ''
  name: x
  type: integer
- container: ''
  name: y
  type: integer
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
- container: set
  name: rules
  type: string
- container: ''
  name: deckType
  type: string
- container: ''
  name: deckConfiguration
  type: string
- container: set
  name: facilities
  type: string
- container: set
  name: seats
  type: string
- container: ''
  name: isChargeable
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
  name: newAircraft
  type: string
- container: ''
  name: arrivalAt
  type: dateTime
- container: ''
  name: departureAt
  type: dateTime
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
  name: lang
  type: string
- container: ''
  name: legSpace
  type: integer
- container: ''
  name: spaceUnit
  type: string
- container: ''
  name: tilt
  type: string
- container: ''
  name: amenityType
  type: string
- container: set
  name: medias
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
  name: address
  type: string
- container: ''
  name: purpose
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
  name: column
  type: string
- container: ''
  name: row
  type: string
- container: ''
  name: position
  type: string
- container: ''
  name: coordinates
  type: string
- container: ''
  name: width
  type: integer
- container: ''
  name: length
  type: integer
- container: ''
  name: startSeatRow
  type: integer
- container: ''
  name: endSeatRow
  type: integer
- container: ''
  name: startWingsX
  type: integer
- container: ''
  name: endWingsX
  type: integer
- container: ''
  name: startWingsRow
  type: integer
- container: ''
  name: endWingsRow
  type: integer
- container: set
  name: exitRowsX
  type: string
- container: set
  name: characteristicsCodes
  type: string
- container: set
  name: travelerPricing
  type: string
- container: ''
  name: self
  type: string
- container: ''
  name: class
  type: string
- container: ''
  name: flightOfferId
  type: string
- container: ''
  name: segmentId
  type: string
- container: set
  name: decks
  type: string
- container: ''
  name: aircraftCabinAmenities
  type: string
- container: set
  name: availableSeatsCounters
  type: string
- container: ''
  name: mediaType
  type: string
- container: ''
  name: value
  type: integer
- container: ''
  name: excessRate
  type: string
- container: ''
  name: quantity
  type: integer
property_count: 136
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
slug: amadeus-seat-map-display-context
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
