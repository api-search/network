---
description: Postal address structure used for shipping, billing, and company addresses
layout: schema
name: Address
properties_list:
- description: Addressee name or attention line
  name: name
  type: string
- description: Street address lines
  name: lines
  type: string
- description: City name
  name: city
  type: string
- description: State or province
  name: state
  type: string
- description: Postal or ZIP code
  name: postalCode
  type: string
- description: Country code (ISO 3166-1 alpha-2)
  name: country
  type: string
- description: Phone number
  name: phone
  type: string
- description: Email address
  name: email
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-address-schema.json
slug: sap-ariba-procurement-address
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: Address
---
