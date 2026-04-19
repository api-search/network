---
description: Percentile bracket contract describing the flight delay for a specific percentile of the distribution
layout: schema
name: PercentileBracketContract
properties_list:
- description: Percentile of the distribution
  name: percentile
  type: integer
- description: 'Delay of the flight for the specific percentile (format: [-]hh:mm:ss).'
  name: delay
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-percentile-bracket-contract-schema.json
slug: aerodatabox-percentile-bracket-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: PercentileBracketContract
---
