---
description: DeliveryAddress schema from Adyen API
layout: schema
name: DeliveryAddress
properties_list:
- description: The name of the city.
  name: city
  type: string
- description: The two-character ISO-3166-1 alpha-2 country code. For example, **US**. >If you don't know the country or are not collecting the country from the shopper, provide `country` as `ZZ`.
  name: country
  type: string
- description: The street name. For example, if the address is "Rokin 49", provide "Rokin".
  name: line1
  type: string
- description: The house number or name. For example, if the address is "Rokin 49", provide "49".
  name: line2
  type: string
- description: Optional information about the address.
  name: line3
  type: string
- description: 'The postal code. Maximum length: * 5 digits for an address in the US. * 10 characters for an address in all other countries.'
  name: postalCode
  type: string
- description: The two-letterISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada. > Required for the US and Canada.
  name: stateOrProvince
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-delivery-address-schema.json
slug: configuration-delivery-address
tags:
- Payments
- Financial Services
- Fintech
title: DeliveryAddress
---
