---
class_count: 22
classes:
- Dimensions
- RateResponse
- ShipmentRequest
- Shipment
- FlightSummary
- FlightStatus
- Member
- RateRequest
- Aircraft
- ScheduleResponse
- AirportList
- ShipmentList
- ShipmentTracking
- TransactionList
- Schedule
- PartnerMilesRequest
- Transaction
- TrackingEvent
- AirportInfo
- FlightList
- Airport
- PartnerMilesResponse
context_file: json-ld/alaska-air-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/json-ld/alaska-air-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Alaska Air from Alaska Airlines.
layout: jsonld
name: Alaska Air Context
namespaces:
- prefix: alaska
  uri: https://alaskaair.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: activityAmount
  type: decimal
- container: ''
  name: activityDate
  type: date
- container: ''
  name: activityType
  type: string
- container: ''
  name: aircraft
  type: string
- container: ''
  name: airportCode
  type: string
- container: ''
  name: airportName
  type: string
- container: set
  name: airports
  type: string
- container: ''
  name: arrivalTime
  type: string
- container: ''
  name: awbNumber
  type: string
- container: ''
  name: cabin
  type: string
- container: ''
  name: carrier
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: commodity
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: currentLocation
  type: string
- container: ''
  name: date
  type: date
- container: ''
  name: delayMinutes
  type: integer
- container: ''
  name: delayReason
  type: string
- container: ''
  name: departureDate
  type: date
- container: ''
  name: departureTime
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: destination
  type: string
- container: ''
  name: destinationAirport
  type: string
- container: ''
  name: dimensions
  type: string
- container: ''
  name: duration
  type: integer
- container: ''
  name: email
  type: string
- container: ''
  name: estimatedArrival
  type: dateTime
- container: ''
  name: estimatedDelivery
  type: date
- container: ''
  name: estimatedDeparture
  type: dateTime
- container: ''
  name: event
  type: string
- container: set
  name: events
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: flightDate
  type: date
- container: ''
  name: flightNumber
  type: string
- container: set
  name: flights
  type: string
- container: ''
  name: gate
  type: string
- container: ''
  name: height
  type: decimal
- container: ''
  name: iataCode
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: latitude
  type: decimal
- container: ''
  name: length
  type: decimal
- container: ''
  name: location
  type: string
- container: ''
  name: longitude
  type: decimal
- container: ''
  name: memberId
  type: string
- container: ''
  name: memberSince
  type: date
- container: ''
  name: mileBalance
  type: integer
- container: ''
  name: miles
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: newBalance
  type: integer
- container: set
  name: operatingDays
  type: string
- container: ''
  name: origin
  type: string
- container: ''
  name: originAirport
  type: string
- container: ''
  name: partner
  type: string
- container: ''
  name: partnerId
  type: string
- container: ''
  name: pieces
  type: integer
- container: ''
  name: ratePerKg
  type: decimal
- container: ''
  name: referenceId
  type: string
- container: ''
  name: scheduledArrival
  type: dateTime
- container: ''
  name: scheduledDeparture
  type: dateTime
- container: set
  name: schedules
  type: string
- container: ''
  name: serviceType
  type: string
- container: ''
  name: shipDate
  type: date
- container: set
  name: shipments
  type: string
- container: set
  name: specialHandling
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: stops
  type: integer
- container: ''
  name: tailNumber
  type: string
- container: ''
  name: terminal
  type: string
- container: ''
  name: tier
  type: string
- container: ''
  name: tierMiles
  type: integer
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: timezone
  type: string
- container: ''
  name: totalCharge
  type: decimal
- container: ''
  name: totalCount
  type: integer
- container: ''
  name: transactionId
  type: string
- container: set
  name: transactions
  type: string
- container: ''
  name: transitDays
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: weight
  type: decimal
- container: ''
  name: weightUnit
  type: string
- container: ''
  name: width
  type: decimal
property_count: 84
provider_name: Alaska Airlines
provider_slug: alaska-air
slug: alaska-air-context
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
- JSON-LD
- Linked Data
- Semantic Web
---
