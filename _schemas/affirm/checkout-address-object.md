---
description: A postal address.
layout: schema
name: AddressObject
properties_list:
- description: Primary street address line.
  name: line1
  type: string
- description: Secondary address line (apartment, suite, unit, etc.).
  name: line2
  type: string
- description: City or locality.
  name: city
  type: string
- description: State, province, or region code.
  name: state
  type: string
- description: Postal or ZIP code.
  name: zipcode
  type: string
- description: ISO 3166-1 alpha-2 country code.
  name: country
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/checkout-address-object-schema.json
slug: checkout-address-object
tags: []
title: AddressObject
---
