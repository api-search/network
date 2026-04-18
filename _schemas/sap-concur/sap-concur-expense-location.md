---
description: A geographic location associated with an expense
layout: schema
name: Location
properties_list:
- description: The location identifier
  name: id
  type: string
- description: The localized location name
  name: name
  type: string
- description: The city name
  name: city
  type: string
- description: ISO 3166-1 alpha-2 country code
  name: countryCode
  type: string
- description: ISO 3166-2 subdivision code
  name: countrySubDivisionCode
  type: string
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-location-schema.json
slug: sap-concur-expense-location
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: Location
---
