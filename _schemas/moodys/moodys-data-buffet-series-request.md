---
description: A single series request within a multi-series call.
layout: schema
name: SeriesRequest
properties_list:
- description: The unique series mnemonic identifier.
  name: mnemonic
  type: string
- description: Desired output frequency.
  name: freq
  type: string
- description: Mathematical transformation to apply.
  name: trans
  type: string
- description: Start date for the data range.
  name: startDate
  type: string
- description: End date for the data range.
  name: endDate
  type: string
- description: Vintage date for historical data revisions.
  name: vintage
  type: string
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-series-request-schema.json
slug: moodys-data-buffet-series-request
tags:
- Climate Risk
- Compliance
- Credit Risk
- Economic Data
- Entity Verification
- Financial Analytics
- Insurance
- KYC
- Risk
- Screening
title: SeriesRequest
---
