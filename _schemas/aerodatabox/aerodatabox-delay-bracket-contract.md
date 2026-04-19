---
description: Delay bracket contract describing how many records are subject to a specific delay range
layout: schema
name: DelayBracketContract
properties_list:
- description: 'The beginning of the delay range (format: [-]hh:mm:ss). E.g. in the expresssion "delayed from 30 to 60 minutes" stands for "from 30 minutes". Value can be negative (therefore, means early occurence). '
  name: delayedFrom
  type: string
- description: 'The end of the delay range (format: [-]hh:mm:ss). E.g. in the expresssion "delayed from 30 to 60 minutes" stands for "to 60 minutes". Value can be negative (therefore, means early occurence). Must be '
  name: delayedTo
  type: string
- description: Count of records subject to a specified delay range
  name: num
  type: integer
- description: Percentage of records subject to a specified delay range. Only available when this delay bracket is provided as a part of a statistical information of a bigger context and the "total" count of records
  name: percentage
  type: number
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-delay-bracket-contract-schema.json
slug: aerodatabox-delay-bracket-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: DelayBracketContract
---
