---
description: ATM detail information
layout: schema
name: Atm
properties_list:
- description: This value indicates under what conditions access fees are charged. Options are UNKNOWN, DOMESTIC, INTERNATIONAL, DOMESTIC_AND_INTERNATIONAL, NO_FEE.
  name: accessFees
  type: string
- description: Line 1 of the street address for the ATM location. Usually includes the street number and name.
  name: addressLine1
  type: string
- description: Line 2 of the street address usually an apartment number or suite number.
  name: addressLine2
  type: string
- description: The Airport Code
  name: airportCode
  type: string
- description: The ATM Terminal Id
  name: atmTerminalId
  type: string
- description: This value indicates the availability hours of the ATM. Options are UNKNOWN, ALWAYS_AVAILABLE, BUSINESS_HOURS, IRREGULAR_HOURS.
  name: availability
  type: string
- description: This value indicates whether or not a security camera is present or near ATM
  name: camera
  type: string
- description: Three digit alpha country code as defined in ISO
  name: countryCode
  type: string
- description: Name of the country.
  name: countryName
  type: string
- description: Code of the state or province for an ATM location.
  name: countrySubdivisionCode
  type: string
- description: Name of the state or province for an ATM location.
  name: countrySubdivisionName
  type: string
- description: The name of the city for an ATM location.
  name: city
  type: string
- description: This is the numerical value for the distance from the provided location to the selected ATM.
  name: distance
  type: number
- description: This is the unit of measure value for the distance from the provided location to the selected ATM. Options are KM and MILE.
  name: distanceUnit
  type: string
- description: GeocodingResult for the ATM
  name: geocodingResult
  type: string
- description: This indicates whether the ATM has the ability to read chip cards or not. Options are UNKNOWN, IS_HANDICAP_ACCESSIBLE, NOT_HANDICAP_ACCESSIBLE.
  name: handicapAccessible
  type: string
- description: This value indicates whether or not the ATM participates in the Mastercard Shared Deposit network. Options are YES or NO.
  name: hasSharedDeposit
  type: string
- description: This value indicates whether or not the ATM participates in the Mastercard Shared (only) Surcharge Free Alliance network. Options are YES or NO.
  name: isSurchargeFreeAlliance
  type: string
- description: The latitude of the ATM
  name: latitude
  type: string
- description: The name of the ATM location
  name: locationName
  type: string
- description: Type of location for the ATM. Options are OTHER, AIRPORT, HOSPITAL, FINANCIAL_INSTITUTION.
  name: locationType
  type: string
- description: The longitude of the ATM.
  name: longitude
  type: string
- description: This is the DBA name of the financial institution affiliate or independent service organization.
  name: owner
  type: string
- description: This is the ICA of the entity that owns the ATM
  name: ownerICA
  type: string
- description: The postal code of the ATM location.
  name: postalCode
  type: string
- description: The routing transaction number
  name: routeTransactionNumber
  type: string
- description: This is the legal or business name of the entity that sponsors the owner of the ATM into the Mastercard network.
  name: sponsor
  type: string
- description: This is the ICA of entity that sponsors the owner of the ATM
  name: sponsorICA
  type: string
- description: This indicates whether the ATM has the ability to read chip cards or not. Options are UNKNOWN, SUPPORTS_EMV, DOES_NOT_SUPPORT_EMV.
  name: supportsEmv
  type: string
- description: This value indicates whether or not the ATM participates in the Mastercard Shared (only) Surcharge Free Alliance network. Options are DOES_NOT_PARTICIPATE_IN_SFA, ALLPOINT_PREPAID, MONEYPASS_DEBIT, an
  name: surchargeFreeAllianceNetwork
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-atm-locations-atm-schema.json
slug: mastercard-atm-locations-atm
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Atm
---
