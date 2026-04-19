---
class_count: 80
classes:
- AirportUrlsContract
- SpeedFlightPlanUnitContract
- SurfaceType
- AirportFlightContract
- FlightAirportMovementContract
- ListingAirportContract
- GeoCoordinatesContractListingAirportContractSearchResultCollectionContract
- Angle
- FlightPlanContract
- ModelFlightTimeEnum
- AirportFidsContract
- SubscriptionSubjectContract
- AirportDelayContract
- FlightDelayContract
- AirportFeedServiceStatusContract
- DistanceFlightPlanUnitContract
- DateTimeContract
- FlightAirportMovementQualityEnum
- FeedServiceStatus
- FlightContract
- AircraftContract
- ErrorContract
- SubscriptionContract
- Pressure
- AirportDistanceTimeContract
- FlightAircraftContract
- SubscriptionSubjectType
- FlightLocationContract
- LicenseType
- StringListingAirportContractSearchResultCollectionContract
- FlightDirection
- GeoCoordinatesContract
- Azimuth
- AircraftContractPagedCollectionContract
- StringFlightSearchItemContractSearchResultCollectionContract
- FlightRules
- ContinentContract
- SolarStateContract
- DailyRouteStatContract
- Speed
- AirportLocalTimeContract
- FlightSearchByEnum
- CountryContract
- DayTime
- AircraftSearchByEnum
- FlightType
- AirportContract
- SubscriptionsBalanceRefillRequestContract
- FlightNotificationItemContract
- FeedServiceEnum
- AirportCodesByEnum
- CreateWebHookSubscription
- FaaLaddAircraftStatusContract
- CodeshareStatus
- FlightLegDelayContract
- PercentileBracketContract
- AircraftRegistrationContract
- FlightAirlineContract
- FlightPlanStatus
- Distance
- SubscriberContract
- EngineType
- DailyRouteStatRecordContract
- StringCollectionContract
- SubscriptionBillingType
- FeedServiceStatusContract
- RunwayContract
- StringAircraftContractSearchResultCollectionContract
- FlightNotificationContract
- StatisticClass
- SubscriptionBalanceContract
- FlightStatus
- FlightSearchItemContract
- ResourceContract
- DelayBracketContract
- FlightDataGeneralAvailabilityContract
- FlightBatchDelayContract
- name
- url
- description
context_file: json-ld/aerodatabox-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/json-ld/aerodatabox-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aerodatabox from AeroDataBox.
layout: jsonld
name: Aerodatabox Context
namespaces:
- prefix: aedbx
  uri: https://aerodatabox.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: webSite
  type: string
- container: ''
  name: wikipedia
  type: string
- container: ''
  name: twitter
  type: string
- container: ''
  name: liveAtc
  type: string
- container: ''
  name: flightRadar
  type: string
- container: ''
  name: googleMaps
  type: string
- container: ''
  name: requested
  type: string
- container: ''
  name: assigned
  type: string
- container: ''
  name: movement
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
  name: callSign
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: codeshareStatus
  type: string
- container: ''
  name: isCargo
  type: boolean
- container: ''
  name: aircraft
  type: string
- container: ''
  name: airline
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: airport
  type: string
- container: ''
  name: scheduledTime
  type: string
- container: ''
  name: revisedTime
  type: string
- container: ''
  name: predictedTime
  type: string
- container: ''
  name: runwayTime
  type: string
- container: ''
  name: terminal
  type: string
- container: ''
  name: checkInDesk
  type: string
- container: ''
  name: gate
  type: string
- container: ''
  name: baggageBelt
  type: string
- container: ''
  name: runway
  type: string
- container: set
  name: quality
  type: string
- container: ''
  name: icao
  type: string
- container: ''
  name: iata
  type: string
- container: ''
  name: localCode
  type: string
- container: ''
  name: shortName
  type: string
- container: ''
  name: municipalityName
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: timeZone
  type: string
- container: ''
  name: searchBy
  type: string
- container: ''
  name: count
  type: integer
- container: set
  name: items
  type: string
- container: ''
  name: deg
  type: decimal
- container: ''
  name: rad
  type: decimal
- container: ''
  name: flightRules
  type: string
- container: ''
  name: flightType
  type: string
- container: ''
  name: revisionNo
  type: integer
- container: ''
  name: route
  type: string
- container: ''
  name: altitude
  type: string
- container: ''
  name: airspeed
  type: string
- container: ''
  name: lastUpdatedUtc
  type: dateTime
- container: set
  name: departures
  type: string
- container: set
  name: arrivals
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: airportIcao
  type: string
- container: ''
  name: from
  type: string
- container: ''
  name: to
  type: string
- container: ''
  name: departuresDelayInformation
  type: string
- container: ''
  name: arrivalsDelayInformation
  type: string
- container: ''
  name: class
  type: string
- container: ''
  name: scheduledHourUtc
  type: integer
- container: ''
  name: medianDelay
  type: string
- container: set
  name: delayPercentiles
  type: string
- container: ''
  name: numConsideredFlights
  type: integer
- container: set
  name: numFlightsDelayedBrackets
  type: string
- container: ''
  name: fromUtc
  type: dateTime
- container: ''
  name: toUtc
  type: dateTime
- container: ''
  name: flightSchedulesFeed
  type: string
- container: ''
  name: liveFlightUpdatesFeed
  type: string
- container: ''
  name: adsbUpdatesFeed
  type: string
- container: ''
  name: generalAvailability
  type: string
- container: ''
  name: utc
  type: dateTime
- container: ''
  name: local
  type: dateTime
- container: ''
  name: greatCircleDistance
  type: string
- container: ''
  name: flightPlan
  type: string
- container: ''
  name: reg
  type: string
- container: ''
  name: active
  type: boolean
- container: ''
  name: serial
  type: string
- container: ''
  name: hexIcao
  type: string
- container: ''
  name: airlineName
  type: string
- container: ''
  name: iataType
  type: string
- container: ''
  name: iataCodeShort
  type: string
- container: ''
  name: icaoCode
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: modelCode
  type: string
- container: ''
  name: numSeats
  type: integer
- container: ''
  name: rolloutDate
  type: dateTime
- container: ''
  name: firstFlightDate
  type: dateTime
- container: ''
  name: deliveryDate
  type: dateTime
- container: ''
  name: registrationDate
  type: dateTime
- container: ''
  name: typeName
  type: string
- container: ''
  name: numEngines
  type: integer
- container: ''
  name: engineType
  type: string
- container: ''
  name: isFreighter
  type: boolean
- container: ''
  name: productionLine
  type: string
- container: ''
  name: ageYears
  type: decimal
- container: ''
  name: verified
  type: boolean
- container: ''
  name: image
  type: string
- container: ''
  name: numRegistrations
  type: integer
- container: set
  name: registrations
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: isActive
  type: boolean
- container: ''
  name: billingType
  type: string
- container: ''
  name: activateBeforeUtc
  type: dateTime
- container: ''
  name: expiresOnUtc
  type: dateTime
- container: ''
  name: createdOnUtc
  type: dateTime
- container: ''
  name: subject
  type: string
- container: ''
  name: subscriber
  type: string
- container: set
  name: notices
  type: string
- container: ''
  name: hPa
  type: decimal
- container: ''
  name: inHg
  type: decimal
- container: ''
  name: mmHg
  type: decimal
- container: ''
  name: approxFlightTime
  type: string
- container: ''
  name: modeS
  type: string
- container: ''
  name: pressureAltitude
  type: string
- container: ''
  name: pressure
  type: string
- container: ''
  name: groundSpeed
  type: string
- container: ''
  name: trueTrack
  type: string
- container: ''
  name: vsiFpm
  type: integer
- container: ''
  name: reportedAtUtc
  type: dateTime
- container: ''
  name: lat
  type: decimal
- container: ''
  name: lon
  type: decimal
- container: ''
  name: totalCount
  type: integer
- container: ''
  name: pageOffset
  type: integer
- container: ''
  name: pageSize
  type: integer
- container: ''
  name: hasNextPage
  type: boolean
- container: ''
  name: code
  type: string
- container: ''
  name: sunElevation
  type: string
- container: ''
  name: sunAzimuth
  type: string
- container: set
  name: dayTime
  type: string
- container: ''
  name: dawnAstronomical
  type: string
- container: ''
  name: dawnNautical
  type: string
- container: ''
  name: dawnCivil
  type: string
- container: ''
  name: sunrise
  type: string
- container: ''
  name: noonTrue
  type: string
- container: ''
  name: sunset
  type: string
- container: ''
  name: duskCivil
  type: string
- container: ''
  name: duskNautical
  type: string
- container: ''
  name: duskAstronomical
  type: string
- container: set
  name: routes
  type: string
- container: ''
  name: kt
  type: decimal
- container: ''
  name: kmPerHour
  type: decimal
- container: ''
  name: miPerHour
  type: decimal
- container: ''
  name: meterPerSecond
  type: decimal
- container: ''
  name: time
  type: string
- container: ''
  name: timeZoneId
  type: string
- container: ''
  name: fullName
  type: string
- container: ''
  name: elevation
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: continent
  type: string
- container: ''
  name: urls
  type: string
- container: set
  name: runways
  type: string
- container: ''
  name: currentTime
  type: string
- container: ''
  name: credits
  type: integer
- container: ''
  name: notificationSummary
  type: string
- container: ''
  name: notificationRemark
  type: string
- container: ''
  name: maxDeliveryRetries
  type: integer
- container: ''
  name: isBlocked
  type: boolean
- container: ''
  name: blockedSince
  type: dateTime
- container: ''
  name: lastBlockedOn
  type: dateTime
- container: set
  name: origins
  type: string
- container: set
  name: destinations
  type: string
- container: ''
  name: percentile
  type: integer
- container: ''
  name: delay
  type: string
- container: ''
  name: meter
  type: decimal
- container: ''
  name: km
  type: decimal
- container: ''
  name: mile
  type: decimal
- container: ''
  name: nm
  type: decimal
- container: ''
  name: feet
  type: decimal
- container: ''
  name: destination
  type: string
- container: ''
  name: averageDailyFlights
  type: decimal
- container: set
  name: operators
  type: string
- container: ''
  name: service
  type: string
- container: ''
  name: minAvailableLocalDate
  type: dateTime
- container: ''
  name: maxAvailableLocalDate
  type: dateTime
- container: ''
  name: trueHdg
  type: decimal
- container: ''
  name: length
  type: string
- container: ''
  name: width
  type: string
- container: ''
  name: isClosed
  type: boolean
- container: ''
  name: surface
  type: string
- container: ''
  name: displacedThreshold
  type: string
- container: ''
  name: hasLighting
  type: boolean
- container: set
  name: flights
  type: string
- container: ''
  name: subscription
  type: string
- container: ''
  name: balance
  type: string
- container: ''
  name: creditsRemaining
  type: integer
- container: ''
  name: lastRefilledUtc
  type: dateTime
- container: ''
  name: lastDeductedUtc
  type: dateTime
- container: ''
  name: webUrl
  type: string
- container: ''
  name: author
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: license
  type: string
- container: set
  name: htmlAttributions
  type: string
- container: ''
  name: delayedFrom
  type: string
- container: ''
  name: delayedTo
  type: string
- container: ''
  name: num
  type: integer
- container: ''
  name: percentage
  type: decimal
- container: ''
  name: numTotal
  type: integer
- container: ''
  name: numQualifiedTotal
  type: integer
- container: ''
  name: numCancelled
  type: integer
- container: ''
  name: delayIndex
  type: decimal
property_count: 200
provider_name: AeroDataBox
provider_slug: aerodatabox
slug: aerodatabox-context
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
- JSON-LD
- Linked Data
- Semantic Web
---
