---
description: Merchant detail information
layout: schema
name: Merchant
properties_list:
- description: Line 1 of the street address for the merchant location. Usually includes the street number and name.
  name: addressLine1
  type: string
- description: Line 2 of the street address usually an apartment number or suite number.
  name: addressLine2
  type: string
- description: Maximum cashback amount permitted at the location.
  name: cashbackMaximumAmount
  type: string
- description: The Merchant Category
  name: category
  type: string
- description: Two digit alpha country code as defined in ISO
  name: countryCode
  type: string
- description: Name of the country.
  name: countryName
  type: string
- description: Code of the state or province for a merchant location.
  name: countrySubdivisionCode
  type: string
- description: Name of the state or province for a merchant location.
  name: countrySubdivisionName
  type: string
- description: The name of the city for a merchant location.
  name: city
  type: string
- description: This is the numerical value for the distance from the provided location to the selected merchant.
  name: distance
  type: number
- description: This is the unit of measure value for the distance from the provided location to the selected merchant. Options are KM and MILE.
  name: distanceUnit
  type: string
- description: Merchant's Easy Savings Offer Id
  name: easySavingsMerchantOfferId
  type: string
- description: GeocodingResult for the merchant
  name: geocodingResult
  type: string
- description: Numerical merchant identifier.
  name: id
  type: integer
- description: Boolean value which indicates if the concession area is equipped with a PayPass card reader.
  name: isPayPassConcession
  type: boolean
- description: Boolean value which indicates if the pharmacy is equipped with a PayPass card reader.
  name: isPayPassPharmacy
  type: boolean
- description: Boolean value which indicates if the fuel pump is equipped with a PayPass card reader.
  name: isPayPassFuelPump
  type: boolean
- description: Boolean value which indicates if the toll booth is equipped with a PayPass card reader.
  name: isPayPassTollBooth
  type: boolean
- description: Boolean value which indicates if the drive thru is equipped with a PayPass card reader.
  name: isPayPassDriveThrough
  type: boolean
- description: Boolean value which indicates if the register is equipped with a PayPass card reader.
  name: isPayPassRegister
  type: boolean
- description: Boolean value which indicates if the ticketing area is equipped with a PayPass card reader.
  name: isPayPassTicketing
  type: boolean
- description: Boolean value which indicates if the vending machine is equipped with a PayPass card reader.
  name: isPayPassVendingMachine
  type: boolean
- description: Boolean value which indicates if the repower card load type at this merchant supports Card Swipe.
  name: isRepowerByCardSwipeSupported
  type: boolean
- description: Boolean value which indicates if the repower card load type at this merchant supports MoneyPak.
  name: isRepowerByMoneyPakSupported
  type: boolean
- description: The latitude of the merchant
  name: latitude
  type: string
- description: The name of the merchant
  name: locationName
  type: string
- description: The longitude of the merchant.
  name: longitude
  type: string
- description: Merchant's phone number
  name: phoneNumber
  type: string
- description: The postal code of the Merchant location.
  name: postalCode
  type: string
- description: Merchant's website URL address
  name: websiteUrl
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-merchant-locations-merchant-schema.json
slug: mastercard-merchant-locations-merchant
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Merchant
---
