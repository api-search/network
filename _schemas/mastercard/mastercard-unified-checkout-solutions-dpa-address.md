---
description: The Digital Payment Application (DPA) business address.
layout: schema
name: DpaAddress
properties_list:
- description: Name of the address
  name: name
  type: string
- description: First line of the address.
  name: line1
  type: string
- description: Second line of the address.
  name: line2
  type: string
- description: Third line of the address.
  name: line3
  type: string
- description: The city/town of the address.
  name: city
  type: string
- description: The state of the address. Use 2-character state designation for USA and Canada addresses.
  name: state
  type: string
- description: ISO 3166 alpha 2 country code. Note that for the UK the correct ISO code is "GB".
  name: countryCode
  type: string
- description: Zipcode for the region.
  name: zip
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-unified-checkout-solutions-dpa-address-schema.json
slug: mastercard-unified-checkout-solutions-dpa-address
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DpaAddress
---
