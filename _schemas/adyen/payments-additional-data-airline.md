---
description: AdditionalDataAirline schema from Adyen API
layout: schema
name: AdditionalDataAirline
properties_list:
- description: 'The reference number for the invoice, issued by the agency. * Encoding: ASCII * minLength: 1 character * maxLength: 6 characters'
  name: airline.agency_invoice_number
  type: string
- description: 'The two-letter agency plan identifier. * Encoding: ASCII * minLength: 2 characters * maxLength: 2 characters'
  name: airline.agency_plan_name
  type: string
- description: 'The [IATA](https://www.iata.org/services/pages/codes.aspx) 3-digit accounting code (PAX) that identifies the carrier. * Format: IATA 3-digit accounting code (PAX) * Example: KLM = 074 * minLength: 3 c'
  name: airline.airline_code
  type: string
- description: 'The [IATA](https://www.iata.org/services/pages/codes.aspx) 2-letter accounting code (PAX) that identifies the carrier. * Encoding: ASCII * Example: KLM = KL * minLength: 2 characters * maxLength: 2 ch'
  name: airline.airline_designator_code
  type: string
- description: 'The amount charged for boarding the plane, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Encoding: Numeric * minLength: 1 character * maxLength: 18 characters'
  name: airline.boarding_fee
  type: string
- description: 'The [CRS](https://en.wikipedia.org/wiki/Computer_reservation_system) used to make the reservation and purchase the ticket. * Encoding: ASCII * minLength: 4 characters * maxLength: 4 characters'
  name: airline.computerized_reservation_system
  type: string
- description: 'The alphanumeric customer reference number. * Encoding: ASCII * maxLength: 20 characters * If you send more than 20 characters, the customer reference number is truncated * Must not be all spaces'
  name: airline.customer_reference_number
  type: string
- description: 'A code that identifies the type of item bought. The description of the code can appear on credit card statements. * Encoding: ASCII * Example: Passenger ticket = 01 * minLength: 2 characters * maxLeng'
  name: airline.document_type
  type: string
- description: 'The flight departure date. Local time `(HH:mm)` is optional. * Date format: `yyyy-MM-dd` * Date and time format: `yyyy-MM-dd HH:mm` * minLength: 10 characters * maxLength: 16 characters'
  name: airline.flight_date
  type: string
- description: 'The [IATA](https://www.iata.org/services/pages/codes.aspx) 2-letter accounting code (PAX) that identifies the carrier. This field is required if the airline data includes leg details. * Example: KLM ='
  name: airline.leg.carrier_code
  type: string
- description: 'A one-letter travel class identifier. The following are common: * F: first class * J: business class * Y: economy class * W: premium economy * Encoding: ASCII * minLength: 1 character * maxLength: 1 c'
  name: airline.leg.class_of_travel
  type: string
- description: 'Date and time of travel in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format `yyyy-MM-dd HH:mm`. * Encoding: ASCII * minLength: 16 characters * maxLength: 16 characters'
  name: airline.leg.date_of_travel
  type: string
- description: 'The [IATA](https://www.iata.org/services/pages/codes.aspx) three-letter airport code of the departure airport. This field is required if the airline data includes leg details. * Encoding: ASCII * Exam'
  name: airline.leg.depart_airport
  type: string
- description: 'The amount of [departure tax](https://en.wikipedia.org/wiki/Departure_tax) charged, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Encoding: Numeric * minLength: 1 * '
  name: airline.leg.depart_tax
  type: string
- description: 'The [IATA](https://www.iata.org/services/pages/codes.aspx) 3-letter airport code of the destination airport. This field is required if the airline data includes leg details. * Example: Amsterdam = AMS'
  name: airline.leg.destination_code
  type: string
- description: 'The [fare basis code](https://en.wikipedia.org/wiki/Fare_basis_code), alphanumeric. * minLength: 1 character * maxLength: 6 characters * Must not be all spaces *Must not be all zeros.'
  name: airline.leg.fare_base_code
  type: string
- description: 'The flight identifier. * minLength: 1 character * maxLength: 5 characters * Must not be all spaces *Must not be all zeros.'
  name: airline.leg.flight_number
  type: string
- description: 'A one-letter code that indicates whether the passenger is entitled to make a stopover. Can be a space, O if the passenger is entitled to make a stopover, or X if they are not. * Encoding: ASCII * minL'
  name: airline.leg.stop_over_code
  type: string
- description: 'The passenger''s date of birth. Date format: `yyyy-MM-dd` * minLength: 10 * maxLength: 10'
  name: airline.passenger.date_of_birth
  type: string
- description: 'The passenger''s first name. > This field is required if the airline data includes passenger details or leg details. * Encoding: ASCII'
  name: airline.passenger.first_name
  type: string
- description: 'The passenger''s last name. > This field is required if the airline data includes passenger details or leg details. * Encoding: ASCII'
  name: airline.passenger.last_name
  type: string
- description: 'The passenger''s telephone number, including country code. This is an alphanumeric field that can include the ''+'' and ''-'' signs. * Encoding: ASCII * minLength: 3 characters * maxLength: 30 characters'
  name: airline.passenger.telephone_number
  type: string
- description: 'The IATA passenger type code (PTC). * Encoding: ASCII * minLength: 3 characters * maxLength: 6 characters'
  name: airline.passenger.traveller_type
  type: string
- description: 'The passenger''s name, initials, and title. * Format: last name + first name or initials + title * Example: *FLYER / MARY MS* * minLength: 1 character * maxLength: 20 characters * If you send more than'
  name: airline.passenger_name
  type: string
- description: 'The address of the organization that issued the ticket. * minLength: 0 characters * maxLength: 16 characters'
  name: airline.ticket_issue_address
  type: string
- description: 'The ticket''s unique identifier. * minLength: 1 character * maxLength: 15 characters * Must not be all spaces *Must not be all zeros.'
  name: airline.ticket_number
  type: string
- description: 'The unique identifier from IATA or ARC for the travel agency that issues the ticket. * Encoding: ASCII * minLength: 1 character * maxLength: 8 characters * Must not be all spaces *Must not be all zero'
  name: airline.travel_agency_code
  type: string
- description: 'The name of the travel agency. * Encoding: ASCII * minLength: 1 character * maxLength: 25 characters * Must not be all spaces *Must not be all zeros.'
  name: airline.travel_agency_name
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-additional-data-airline-schema.json
slug: payments-additional-data-airline
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataAirline
---
