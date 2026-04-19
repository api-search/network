---
description: AdditionalDataLodging schema from Adyen API
layout: schema
name: AdditionalDataLodging
properties_list:
- description: 'The arrival date. * Date format: **yyyyMmDd**. For example, for 2023 April 22, **20230422**.'
  name: lodging.checkInDate
  type: string
- description: 'The departure date. * Date format: **yyyyMmDd**. For example, for 2023 April 22, **20230422**.'
  name: lodging.checkOutDate
  type: string
- description: 'The toll-free phone number for the lodging. * Format: numeric * Max length: 17 characters. * For US and CA numbers must be 10 characters in length * Must not start with a space * Must not contain any '
  name: lodging.customerServiceTollFreeNumber
  type: string
- description: 'Identifies that the facility complies with the Hotel and Motel Fire Safety Act of 1990. Must be ''Y'' or ''N''. * Format: alphabetic * Max length: 1 character'
  name: lodging.fireSafetyActIndicator
  type: string
- description: 'The folio cash advances, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters'
  name: lodging.folioCashAdvances
  type: string
- description: 'The card acceptor’s internal invoice or billing ID reference number. * Max length: 25 characters. * Must not start with a space *Must not be all zeros.'
  name: lodging.folioNumber
  type: string
- description: 'Any charges for food and beverages associated with the booking, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters'
  name: lodging.foodBeverageCharges
  type: string
- description: 'Indicates if the customer didn''t check in for their booking. Possible values: * **Y**: the customer didn''t check in * **N**: the customer checked in'
  name: lodging.noShowIndicator
  type: string
- description: 'The prepaid expenses for the booking. * Format: numeric * Max length: 12 characters'
  name: lodging.prepaidExpenses
  type: string
- description: 'The lodging property location''s phone number. * Format: numeric. * Min length: 10 characters * Max length: 17 characters * For US and CA numbers must be 10 characters in length * Must not start with a'
  name: lodging.propertyPhoneNumber
  type: string
- description: 'The total number of nights the room is booked for. * Format: numeric * Must be a number between 0 and 99 * Max length: 4 characters'
  name: lodging.room1.numberOfNights
  type: string
- description: 'The rate for the room, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters * Must not be a negative number'
  name: lodging.room1.rate
  type: string
- description: 'The total room tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters * Must not be a negative number'
  name: lodging.totalRoomTax
  type: string
- description: 'The total tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters * Must not be a negative number'
  name: lodging.totalTax
  type: string
- description: 'The number of nights. This should be included in the auth message. * Format: numeric * Max length: 4 characters'
  name: travelEntertainmentAuthData.duration
  type: string
- description: 'Indicates what market-specific dataset will be submitted. Must be ''H'' for Hotel. This should be included in the auth message. * Format: alphanumeric * Max length: 1 character'
  name: travelEntertainmentAuthData.market
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-additional-data-lodging-schema.json
slug: checkout-additional-data-lodging
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataLodging
---
