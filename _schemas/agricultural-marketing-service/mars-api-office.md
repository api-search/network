---
description: A USDA AMS market news office.
layout: schema
name: Office
properties_list:
- description: Unique identifier for the office.
  name: office_id
  type: string
- description: Name of the market news office.
  name: name
  type: string
- description: City where the office is located.
  name: city
  type: string
- description: State where the office is located.
  name: state
  type: string
- description: List of commodities covered by this office.
  name: commodities
  type: array
provider_name: Agricultural Marketing Service
provider_slug: agricultural-marketing-service
schema_file: json-schema/mars-api-office-schema.json
slug: mars-api-office
tags:
- Agriculture
- Federal Government
- Market News
- Livestock
- Dairy
- Fruits And Vegetables
- Cotton
- Tobacco
title: Office
---
