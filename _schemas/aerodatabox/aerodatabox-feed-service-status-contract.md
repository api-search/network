---
description: Feed service status contract. Read https://aerodatabox.com/data-coverage for context.
layout: schema
name: FeedServiceStatusContract
properties_list:
- description: ''
  name: service
  type: object
- description: ''
  name: status
  type: object
- description: Date of the oldest flight stored (based on scheduled local times)
  name: minAvailableLocalDate
  type: string
- description: Date of the most recent flight stored (based on scheduled local times)
  name: maxAvailableLocalDate
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-feed-service-status-contract-schema.json
slug: aerodatabox-feed-service-status-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FeedServiceStatusContract
---
