---
description: A merchant or card acceptor registered in the Mastercard network. Represents businesses that accept Mastercard payments, with location, categorization, and terminal capability data. Used across Merchant Locations, Checkout Solutions, fraud reporting, and analytics APIs.
layout: schema
name: Mastercard Merchant
properties_list:
- description: Card acceptor or merchant unique identification number assigned by the acquirer.
  name: merchantId
  type: string
- description: Numerical merchant identifier within the Mastercard Merchant Locations system.
  name: id
  type: integer
- description: Legal or trade name of the merchant.
  name: merchantName
  type: string
- description: Doing Business As (DBA) name, the merchant name visible to cardholders.
  name: dbaName
  type: string
- description: Four-digit ISO 18245 Merchant Category Code (MCC) classifying the business type.
  name: merchantCategoryCode
  type: string
- description: Human-readable merchant category description from the Mastercard category taxonomy.
  name: category
  type: string
- description: Mastercard internal category identifier for the merchant.
  name: categoryId
  type: string
- description: Classification of the merchant by acceptance capability.
  name: merchantType
  type: string
- description: ''
  name: address
  type: object
- description: ''
  name: location
  type: object
- description: Distance from a search reference point to this merchant location.
  name: distance
  type: number
- description: Unit of measure for the distance value.
  name: distanceUnit
  type: string
- description: Geocoding result quality indicator for the merchant address.
  name: geocodingResult
  type: string
- description: ''
  name: terminalCapabilities
  type: object
- description: Maximum cashback amount permitted at this merchant location.
  name: cashbackMaximumAmount
  type: string
- description: ''
  name: dpa
  type: object
- description: ICA number of the acquiring institution for this merchant.
  name: acquirerId
  type: string
- description: Merchant identifier assigned by the acquirer.
  name: acquirerMerchantId
  type: string
- description: URL of the merchant website.
  name: websiteUrl
  type: string
- description: URL of the merchant logo image.
  name: logoUrl
  type: string
- description: Unique identifier representing the merchant as a sponsor of offers.
  name: offerMerchantId
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/merchant.json
slug: merchant
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Mastercard Merchant
---
