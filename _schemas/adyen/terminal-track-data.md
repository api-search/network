---
description: ISO 7813 - ISO 4909. Generic data structure for a card track, used when the magstripe card reader is located on the Sale Terminal, or for magstripe Card Reader device request. The data structure is also used to store the line at the bottom of a bank check. Magnetic track or magnetic ink characters line.
layout: schema
name: TrackData
properties_list:
- description: ''
  name: TrackNumb
  type: integer
- description: ''
  name: TrackFormat
  type: object
- description: ''
  name: TrackValue
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-track-data-schema.json
slug: terminal-track-data
tags:
- Payments
- Financial Services
- Fintech
title: TrackData
---
