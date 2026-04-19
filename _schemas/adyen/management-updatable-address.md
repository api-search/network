---
description: UpdatableAddress schema from Adyen API
layout: schema
name: UpdatableAddress
properties_list:
- description: The name of the city.
  name: city
  type: string
- description: The street address.
  name: line1
  type: string
- description: Second address line.
  name: line2
  type: string
- description: Third address line.
  name: line3
  type: string
- description: The postal code.
  name: postalCode
  type: string
- description: 'The state or province code as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada. Required for the following countries: - Australia - Brazil - Ca'
  name: stateOrProvince
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-updatable-address-schema.json
slug: management-updatable-address
tags:
- Payments
- Financial Services
- Fintech
title: UpdatableAddress
---
