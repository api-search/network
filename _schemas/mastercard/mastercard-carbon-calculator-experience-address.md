---
description: ''
layout: schema
name: Address
properties_list:
- description: Denotes three-character country code.
  name: countryCode
  type: string
- description: Neighborhood.
  name: locality
  type: string
- description: <p> The postal code in the address is the ZIP code or equivalent and can be an alphanumeric value including whitespace (for example, PE7 8FT). <br><b> Note - Special characters and only whitespace cha
  name: postalCode
  type: string
- description: The state or region or province to which the address belongs.
  name: state
  type: string
- description: City.
  name: city
  type: string
- description: Street Address line1.
  name: line1
  type: string
- description: Street Address line2.
  name: line2
  type: string
- description: Street Address line3.
  name: line3
  type: string
- description: Denotes the type of address. (For example, home or work)
  name: type
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-carbon-calculator-experience-address-schema.json
slug: mastercard-carbon-calculator-experience-address
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Address
---
