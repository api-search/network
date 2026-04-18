---
description: The Digital Payment Application (DPA) business address.
layout: schema
name: Address
properties_list:
- description: Contact name for the address.
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
- description: Address of city
  name: city
  type: string
- description: Address of state
  name: state
  type: string
- description: Address country code. ISO 3166 alpha 2 country code.
  name: countryCode
  type: string
- description: Address zip/postal code.
  name: zip
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-address-schema.json
slug: mastercard-checkout-solutions-address
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Address
---
