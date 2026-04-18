---
description: Merchant Search Request Info
layout: schema
name: MerchantSearch
properties_list:
- description: Line 1 of the street address for the merchant location. Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you
  name: addressLine1
  type: string
- description: Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must al
  name: addressLine2
  type: string
- description: The name of the city for a merchant location. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
  name: city
  type: string
- description: Any two digit country code for a Merchant location. Valid values are two digit alpha country code. This parameter is ignored if latitude and longitude are provided. This parameter is required if any o
  name: countryCode
  type: string
- description: The state or province for a merchant location (only supported for US and Canada locations). This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must als
  name: countrySubdivisionCode
  type: string
- description: The latitude of a merchant location. If latitude is provided longitude must also be provided.
  name: latitude
  type: string
- description: The longitude of a merchant location. If longitude is provided latitude must also be provided.
  name: longitude
  type: string
- description: Category Id of the merchant location. See the Categories resource for a list of valid categories. Input may be a comma delimited list of category ids.
  name: merchantCategory
  type: string
- description: Type of merchant location. Options are 'paypass' 'repower' 'easysavings' and 'cashback'.
  name: merchantType
  type: string
- description: Unique identifier that represents the merchant sponsor of an offer. Any valid merchant ID.
  name: offerMerchantId
  type: string
- description: The zip code or postal code for a Merchant location. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
  name: postalCode
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-merchant-locations-merchant-search-schema.json
slug: mastercard-merchant-locations-merchant-search
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: MerchantSearch
---
