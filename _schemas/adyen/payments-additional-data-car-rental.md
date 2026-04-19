---
description: AdditionalDataCarRental schema from Adyen API
layout: schema
name: AdditionalDataCarRental
properties_list:
- description: 'The pick-up date. * Date format: `yyyyMMdd`'
  name: carRental.checkOutDate
  type: string
- description: 'The customer service phone number of the car rental company. * Format: Alphanumeric * maxLength: 17 * For US and CA numbers must be 10 characters in length * Must not start with a space * Must not con'
  name: carRental.customerServiceTollFreeNumber
  type: string
- description: 'Number of days for which the car is being rented. * Format: Numeric * maxLength: 4 * Must not be all spaces'
  name: carRental.daysRented
  type: string
- description: 'Any fuel charges associated with the rental, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: Numeric * maxLength: 12'
  name: carRental.fuelCharges
  type: string
- description: 'Any insurance charges associated with the rental, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: Numeric * maxLength: 12 * Must not be all spaces *Must not be'
  name: carRental.insuranceCharges
  type: string
- description: 'The city where the car is rented. * Format: Alphanumeric * maxLength: 18 * Must not start with a space or be all spaces *Must not be all zeros.'
  name: carRental.locationCity
  type: string
- description: 'The country where the car is rented, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. * Format: Alphanumeric * maxLength: 2'
  name: carRental.locationCountry
  type: string
- description: 'The state or province where the car is rented. * Format: Alphanumeric * maxLength: 2 * Must not start with a space or be all spaces *Must not be all zeros.'
  name: carRental.locationStateProvince
  type: string
- description: Indicates if the customer didn't pick up their rental car. * Y - Customer did not pick up their car * N - Not applicable
  name: carRental.noShowIndicator
  type: string
- description: 'The charge for not returning a car to the original rental location, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * maxLength: 12'
  name: carRental.oneWayDropOffCharges
  type: string
- description: 'The daily rental rate, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: Alphanumeric * maxLength: 12'
  name: carRental.rate
  type: string
- description: Specifies whether the given rate is applied daily or weekly. * D - Daily rate * W - Weekly rate
  name: carRental.rateIndicator
  type: string
- description: 'The rental agreement number for the car rental. * Format: Alphanumeric * maxLength: 9 * Must not start with a space or be all spaces *Must not be all zeros.'
  name: carRental.rentalAgreementNumber
  type: string
- description: 'The classification of the rental car. * Format: Alphanumeric * maxLength: 4 * Must not start with a space or be all spaces *Must not be all zeros.'
  name: carRental.rentalClassId
  type: string
- description: 'The name of the person renting the car. * Format: Alphanumeric * maxLength: 26 * If you send more than 26 characters, the name is truncated * Must not start with a space or be all spaces *Must not be '
  name: carRental.renterName
  type: string
- description: 'The city where the car must be returned. * Format: Alphanumeric * maxLength: 18 * Must not start with a space or be all spaces *Must not be all zeros.'
  name: carRental.returnCity
  type: string
- description: 'The country where the car must be returned, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. * Format: Alphanumeric * maxLength: 2'
  name: carRental.returnCountry
  type: string
- description: 'The last date to return the car by. * Date format: `yyyyMMdd` * maxLength: 8'
  name: carRental.returnDate
  type: string
- description: 'The agency code, phone number, or address abbreviation * Format: Alphanumeric * maxLength: 10 * Must not start with a space or be all spaces *Must not be all zeros.'
  name: carRental.returnLocationId
  type: string
- description: 'The state or province where the car must be returned. * Format: Alphanumeric * maxLength: 3 * Must not start with a space or be all spaces *Must not be all zeros.'
  name: carRental.returnStateProvince
  type: string
- description: 'Indicates if the goods or services were tax-exempt, or if tax was not paid on them. Values: * Y - Goods or services were tax exempt * N - Tax was not collected'
  name: carRental.taxExemptIndicator
  type: string
- description: 'Number of days the car is rented for. This should be included in the auth message. * Format: Numeric * maxLength: 4'
  name: travelEntertainmentAuthData.duration
  type: string
- description: 'Indicates what market-specific dataset will be submitted or is being submitted. Value should be ''A'' for car rental. This should be included in the auth message. * Format: Alphanumeric * maxLength: 1'
  name: travelEntertainmentAuthData.market
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-additional-data-car-rental-schema.json
slug: payments-additional-data-car-rental
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataCarRental
---
