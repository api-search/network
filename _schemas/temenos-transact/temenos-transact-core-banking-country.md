---
description: Country definition with regulatory details
layout: schema
name: Country
properties_list:
- description: ISO 3166-1 alpha-2 country code
  name: countryCode
  type: string
- description: Full country name
  name: countryName
  type: string
- description: Default currency code
  name: currencyCode
  type: string
- description: Whether IBAN is required for payments to this country
  name: ibanRequired
  type: boolean
- description: Whether the country is under sanctions
  name: sanctioned
  type: boolean
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-country-schema.json
slug: temenos-transact-core-banking-country
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Country
---
