---
class_count: 46
classes:
- TicketingAgreement
- Price
- ChargeableSeat
- AirlineRemark
- FormOfIdentification
- Extended_Price
- Co2Emission
- BaggageAllowance
- GeneralRemark
- AirTravelDocumentCommon
- Tax
- Collection_Meta_Link
- FormOfPayment
- BaseName
- Fee
- Error_400
- AssociatedRecordCommon
- Address
- Dictionaries
- Phone
- Stakeholder
- Remarks
- Error_500
- OriginalFlightStop
- OtherMethod
- Document
- EmergencyContact
- CreditCardCommon
- FlightSegment
- CreditCard
- Issue
- AircraftEquipment
- ContactDictionary
- FlightOrder
- B2bWallet
- LoyaltyProgram
- ElementaryPrice
- OriginalFlightEndPoint
- AllotmentDetails
- LocationValue
- FlightOffer
- Error_404
- AutomatedProcessCommon
- Discount
- OperatingFlight
- name
context_file: json-ld/amadeus-flight-order-management-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/json-ld/amadeus-flight-order-management-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Flight Order Management from Amadeus Reservations.
layout: jsonld
name: Amadeus Flight Order Management Context
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
  name: option
  type: string
- container: ''
  name: delay
  type: string
- container: ''
  name: dateTime
  type: string
- container: set
  name: segmentIds
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
  name: id
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: subType
  type: string
- container: ''
  name: keyword
  type: string
- container: ''
  name: airlineCode
  type: string
- container: ''
  name: text
  type: string
- container: set
  name: travelerIds
  type: string
- container: set
  name: flightOfferIds
  type: string
- container: ''
  name: identificationType
  type: string
- container: ''
  name: carrierCode
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
  name: quantity
  type: integer
- container: ''
  name: category
  type: string
- container: ''
  name: documentType
  type: string
- container: ''
  name: documentNumber
  type: string
- container: ''
  name: documentStatus
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: count
  type: integer
- container: ''
  name: links
  type: reference
- container: ''
  name: b2bWallet
  type: string
- container: ''
  name: creditCard
  type: string
- container: ''
  name: other
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
  name: type
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: creationDate
  type: string
- container: ''
  name: originSystemCode
  type: string
- container: set
  name: lines
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: countryCode
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
  name: deviceType
  type: string
- container: ''
  name: countryCallingCode
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
- container: set
  name: general
  type: string
- container: set
  name: airline
  type: string
- container: ''
  name: iataCode
  type: string
- container: ''
  name: duration
  type: string
- container: ''
  name: method
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
  name: addresseeName
  type: string
- container: ''
  name: brand
  type: string
- container: ''
  name: holder
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
  name: bookingStatus
  type: string
- container: ''
  name: segmentType
  type: string
- container: ''
  name: isFlown
  type: boolean
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
  type: reference
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
  name: queuingOfficeId
  type: string
- container: ''
  name: ownerOfficeId
  type: string
- container: set
  name: associatedRecords
  type: string
- container: set
  name: flightOffers
  type: string
- container: set
  name: travelers
  type: string
- container: ''
  name: remarks
  type: string
- container: set
  name: formOfPayments
  type: string
- container: ''
  name: ticketingAgreement
  type: string
- container: set
  name: automatedProcess
  type: string
- container: set
  name: contacts
  type: string
- container: set
  name: tickets
  type: string
- container: set
  name: formOfIdentifications
  type: string
- container: ''
  name: cardId
  type: string
- container: ''
  name: cardUsageName
  type: string
- container: ''
  name: cardFriendlyName
  type: string
- container: set
  name: reportingData
  type: ''
- container: ''
  name: virtualCreditCardDetails
  type: string
- container: ''
  name: programOwner
  type: string
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: terminal
  type: string
- container: ''
  name: tourName
  type: string
- container: ''
  name: tourReference
  type: string
- container: ''
  name: cityCode
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
  type: ''
- container: ''
  name: price
  type: string
- container: ''
  name: pricingOptions
  type: reference
- container: set
  name: validatingAirlineCodes
  type: string
- container: set
  name: travelerPricings
  type: string
- container: ''
  name: queue
  type: reference
- container: ''
  name: travelerType
  type: string
- container: ''
  name: cardNumber
  type: string
- container: ''
  name: certificateNumber
  type: string
property_count: 126
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
slug: amadeus-flight-order-management-context
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
- JSON-LD
- Linked Data
- Semantic Web
---
