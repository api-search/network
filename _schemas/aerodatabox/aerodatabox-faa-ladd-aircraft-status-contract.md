---
description: Status of the aircraft tail number or callsign in the FAA Limiting Aircraft Data Displayed (LADD) Program list. See https://www.faa.gov/pilots/ladd for more details.
layout: schema
name: FaaLaddAircraftStatusContract
properties_list:
- description: ''
  name: id
  type: string
- description: Current status of the aircraft / flight in the FAA LADD industry list.
  name: isBlocked
  type: boolean
- description: 'For blocked aircraft only: the date when the aircraft / flight was blocked. Will not be included for blocked dates at or prior to September 15, 2024.'
  name: blockedSince
  type: string
- description: 'For unblocked aircraft only: the date when the aircraft / flight was last blocked. Will not be included for blocked dates at or prior to September 15, 2024 or for the aircraft that were never blocked.'
  name: lastBlockedOn
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-faa-ladd-aircraft-status-contract-schema.json
slug: aerodatabox-faa-ladd-aircraft-status-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FaaLaddAircraftStatusContract
---
